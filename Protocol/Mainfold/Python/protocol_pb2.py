# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eprotocol.proto\" \n\x08PosPoint\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\x83\x01\n\nScanResult\x12\x1b\n\x08position\x18\x01 \x03(\x0b\x32\t.PosPoint\x12\x1e\n\x0bpicrutesize\x18\x04 \x01(\x0b\x32\t.PosPoint\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\r\n\x05\x61ngle\x18\x03 \x01(\x02\x12\x19\n\x06\x63\x65nter\x18\x05 \x01(\x0b\x32\t.PosPoint\"(\n\x07PadPass\x12\x0b\n\x03pad\x18\x01 \x01(\x0c\x12\x10\n\x08password\x18\x02 \x01(\x0c\"\xf9\x01\n\x0bVideoRecord\x12)\n\x07\x63ontrol\x18\x01 \x01(\x0e\x32\x18.VideoRecord.ControlType\x12\'\n\x06status\x18\x02 \x01(\x0e\x32\x17.VideoRecord.StatusType\x12\x12\n\nDeviceName\x18\x03 \x01(\t\x12\x10\n\x08\x44\x65viceId\x18\x04 \x01(\t\x12\x10\n\x08Operator\x18\x05 \x01(\t\"8\n\x0b\x43ontrolType\x12\x08\n\x04NULL\x10\x00\x12\t\n\x05Start\x10\x01\x12\x08\n\x04Stop\x10\x02\x12\n\n\x06Status\x10\x03\"$\n\nStatusType\x12\r\n\tRecording\x10\x00\x12\x07\n\x03Off\x10\x01\"\x1c\n\nUltraSonic\x12\x0e\n\x06height\x18\x01 \x01(\x02\"\x99\x01\n\x07Message\x12)\n\x0bmessagetype\x18\x01 \x01(\x0e\x32\x14.Message.MessageType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"U\n\x0bMessageType\x12\x08\n\x04NULL\x10\x00\x12\x0e\n\nScanResult\x10\x01\x12\x0b\n\x07PadPass\x10\x02\x12\x0f\n\x0bVideoRecord\x10\x03\x12\x0e\n\nUltraSonic\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VIDEORECORD_CONTROLTYPE = _descriptor.EnumDescriptor(
  name='ControlType',
  full_name='VideoRecord.ControlType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Start', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Stop', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Status', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=384,
  serialized_end=440,
)
_sym_db.RegisterEnumDescriptor(_VIDEORECORD_CONTROLTYPE)

_VIDEORECORD_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='VideoRecord.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Recording', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Off', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=442,
  serialized_end=478,
)
_sym_db.RegisterEnumDescriptor(_VIDEORECORD_STATUSTYPE)

_MESSAGE_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='Message.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ScanResult', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PadPass', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VideoRecord', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UltraSonic', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=579,
  serialized_end=664,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_MESSAGETYPE)


_POSPOINT = _descriptor.Descriptor(
  name='PosPoint',
  full_name='PosPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PosPoint.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='PosPoint.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=50,
)


_SCANRESULT = _descriptor.Descriptor(
  name='ScanResult',
  full_name='ScanResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='ScanResult.position', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='picrutesize', full_name='ScanResult.picrutesize', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='ScanResult.result', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle', full_name='ScanResult.angle', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center', full_name='ScanResult.center', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=184,
)


_PADPASS = _descriptor.Descriptor(
  name='PadPass',
  full_name='PadPass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pad', full_name='PadPass.pad', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='PadPass.password', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=226,
)


_VIDEORECORD = _descriptor.Descriptor(
  name='VideoRecord',
  full_name='VideoRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control', full_name='VideoRecord.control', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='VideoRecord.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeviceName', full_name='VideoRecord.DeviceName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeviceId', full_name='VideoRecord.DeviceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Operator', full_name='VideoRecord.Operator', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VIDEORECORD_CONTROLTYPE,
    _VIDEORECORD_STATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=478,
)


_ULTRASONIC = _descriptor.Descriptor(
  name='UltraSonic',
  full_name='UltraSonic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='UltraSonic.height', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=508,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messagetype', full_name='Message.messagetype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Message.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_MESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=664,
)

_SCANRESULT.fields_by_name['position'].message_type = _POSPOINT
_SCANRESULT.fields_by_name['picrutesize'].message_type = _POSPOINT
_SCANRESULT.fields_by_name['center'].message_type = _POSPOINT
_VIDEORECORD.fields_by_name['control'].enum_type = _VIDEORECORD_CONTROLTYPE
_VIDEORECORD.fields_by_name['status'].enum_type = _VIDEORECORD_STATUSTYPE
_VIDEORECORD_CONTROLTYPE.containing_type = _VIDEORECORD
_VIDEORECORD_STATUSTYPE.containing_type = _VIDEORECORD
_MESSAGE.fields_by_name['messagetype'].enum_type = _MESSAGE_MESSAGETYPE
_MESSAGE_MESSAGETYPE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['PosPoint'] = _POSPOINT
DESCRIPTOR.message_types_by_name['ScanResult'] = _SCANRESULT
DESCRIPTOR.message_types_by_name['PadPass'] = _PADPASS
DESCRIPTOR.message_types_by_name['VideoRecord'] = _VIDEORECORD
DESCRIPTOR.message_types_by_name['UltraSonic'] = _ULTRASONIC
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

PosPoint = _reflection.GeneratedProtocolMessageType('PosPoint', (_message.Message,), dict(
  DESCRIPTOR = _POSPOINT,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:PosPoint)
  ))
_sym_db.RegisterMessage(PosPoint)

ScanResult = _reflection.GeneratedProtocolMessageType('ScanResult', (_message.Message,), dict(
  DESCRIPTOR = _SCANRESULT,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:ScanResult)
  ))
_sym_db.RegisterMessage(ScanResult)

PadPass = _reflection.GeneratedProtocolMessageType('PadPass', (_message.Message,), dict(
  DESCRIPTOR = _PADPASS,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:PadPass)
  ))
_sym_db.RegisterMessage(PadPass)

VideoRecord = _reflection.GeneratedProtocolMessageType('VideoRecord', (_message.Message,), dict(
  DESCRIPTOR = _VIDEORECORD,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:VideoRecord)
  ))
_sym_db.RegisterMessage(VideoRecord)

UltraSonic = _reflection.GeneratedProtocolMessageType('UltraSonic', (_message.Message,), dict(
  DESCRIPTOR = _ULTRASONIC,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:UltraSonic)
  ))
_sym_db.RegisterMessage(UltraSonic)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
