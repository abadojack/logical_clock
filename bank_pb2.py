# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bank.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbank.proto\"\x84\x01\n\x12MsgDeliveryRequest\x12\r\n\x05money\x18\x01 \x01(\x03\x12\"\n\x0crequest_type\x18\x02 \x01(\x0e\x32\x0c.RequestType\x12\x12\n\nrequest_id\x18\x03 \x01(\x03\x12\x18\n\x10\x62ranch_client_id\x18\x04 \x01(\x03\x12\r\n\x05\x63lock\x18\x05 \x01(\x03\"a\n\x13MsgDeliveryResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05money\x18\x02 \x01(\x01\x12 \n\x0bstatus_code\x18\x03 \x01(\x0e\x32\x0b.StatusCode\x12\r\n\x05\x63lock\x18\x04 \x01(\x03*3\n\x0bRequestType\x12\t\n\x05QUERY\x10\x00\x12\x0b\n\x07\x44\x45POSIT\x10\x01\x12\x0c\n\x08WITHDRAW\x10\x02*1\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x32\x42\n\x04\x42\x61nk\x12:\n\x0bMsgDelivery\x12\x13.MsgDeliveryRequest\x1a\x14.MsgDeliveryResponse\"\x00\x62\x06proto3'
)

_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='RequestType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WITHDRAW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=248,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_REQUESTTYPE)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='StatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=301,
  serialized_end=350,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
QUERY = 0
DEPOSIT = 1
WITHDRAW = 2
SUCCESS = 0
FAILURE = 1
ERROR = 2



_MSGDELIVERYREQUEST = _descriptor.Descriptor(
  name='MsgDeliveryRequest',
  full_name='MsgDeliveryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='money', full_name='MsgDeliveryRequest.money', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='MsgDeliveryRequest.request_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='MsgDeliveryRequest.request_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='branch_client_id', full_name='MsgDeliveryRequest.branch_client_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clock', full_name='MsgDeliveryRequest.clock', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=147,
)


_MSGDELIVERYRESPONSE = _descriptor.Descriptor(
  name='MsgDeliveryResponse',
  full_name='MsgDeliveryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MsgDeliveryResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='money', full_name='MsgDeliveryResponse.money', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='MsgDeliveryResponse.status_code', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clock', full_name='MsgDeliveryResponse.clock', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=246,
)

_MSGDELIVERYREQUEST.fields_by_name['request_type'].enum_type = _REQUESTTYPE
_MSGDELIVERYRESPONSE.fields_by_name['status_code'].enum_type = _STATUSCODE
DESCRIPTOR.message_types_by_name['MsgDeliveryRequest'] = _MSGDELIVERYREQUEST
DESCRIPTOR.message_types_by_name['MsgDeliveryResponse'] = _MSGDELIVERYRESPONSE
DESCRIPTOR.enum_types_by_name['RequestType'] = _REQUESTTYPE
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgDeliveryRequest = _reflection.GeneratedProtocolMessageType('MsgDeliveryRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGDELIVERYREQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:MsgDeliveryRequest)
  })
_sym_db.RegisterMessage(MsgDeliveryRequest)

MsgDeliveryResponse = _reflection.GeneratedProtocolMessageType('MsgDeliveryResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGDELIVERYRESPONSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:MsgDeliveryResponse)
  })
_sym_db.RegisterMessage(MsgDeliveryResponse)



_BANK = _descriptor.ServiceDescriptor(
  name='Bank',
  full_name='Bank',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=352,
  serialized_end=418,
  methods=[
  _descriptor.MethodDescriptor(
    name='MsgDelivery',
    full_name='Bank.MsgDelivery',
    index=0,
    containing_service=None,
    input_type=_MSGDELIVERYREQUEST,
    output_type=_MSGDELIVERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BANK)

DESCRIPTOR.services_by_name['Bank'] = _BANK

# @@protoc_insertion_point(module_scope)