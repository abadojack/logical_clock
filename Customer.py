import time
import datetime
import multiprocessing
import json
from concurrent import futures
import grpc
import bank_pb2
import bank_pb2_grpc   

operation = {
    "query": bank_pb2.QUERY,
    "deposit": bank_pb2.DEPOSIT,
    "withdraw": bank_pb2.WITHDRAW
}

client_lock = multiprocessing.Lock()

class Customer:
    def __init__(self, _id, events):
        # unique ID of the Customer
        self.id = _id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None

    def createStub(self, Branch_address):
        self.stub = bank_pb2_grpc.BankStub(grpc.insecure_channel(Branch_address))

        client = grpc.server(futures.ThreadPoolExecutor(max_workers=1,),)
        client.start()

    def executeEvents(self, output_file):      
        record = {'id': self.id, 'recv': []}
        for event in self.events:
            request_id = event['id']
            request_operation = operation[event['interface']]
            request_amount = event['money']
            
            try:

                response = self.stub.MsgDelivery(
                    bank_pb2.MsgDeliveryRequest(
                        request_id=request_id,
                        request_type=request_operation,
                        money=request_amount,
                        branch_client_id=self.id,
                        clock=0
                    )
                )

                if request_operation == bank_pb2.QUERY:
                    values['money'] = response.money
                record['recv'].append(values)
                                 
                if record['recv']:
                    with open(f'{output_file}', 'a') as outfile:
                        json.dump(record, outfile)
                        outfile.write('\n')
                        
            except grpc.RpcError as rpc_error_call:
                pass

    def run_customer(self, Branch_address, output_file):
        Customer.createStub(self, Branch_address)
        Customer.executeEvents(self, output_file)
