# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rMessage.proto\x12\x0emessagePackage\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0c\x45\x63hoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2P\n\x0b\x45\x63hoService\x12\x41\n\x04\x65\x63ho\x12\x1b.messagePackage.EchoRequest\x1a\x1c.messagePackage.EchoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ECHOREQUEST']._serialized_start=33
  _globals['_ECHOREQUEST']._serialized_end=63
  _globals['_ECHORESPONSE']._serialized_start=65
  _globals['_ECHORESPONSE']._serialized_end=96
  _globals['_ECHOSERVICE']._serialized_start=98
  _globals['_ECHOSERVICE']._serialized_end=178
# @@protoc_insertion_point(module_scope)
