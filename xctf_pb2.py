# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xctf/xctf.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fxctf/xctf.proto\x12\x04xctf\"\x07\n\x05\x45mpty\"R\n\x16UpsertChallengeRequest\x12$\n\rchallengeName\x18\x01 \x01(\tR\rchallengeName\x12\x12\n\x04\x66lag\x18\x02 \x01(\tR\x04\x66lag\">\n\x16\x44\x65leteChallengeRequest\x12$\n\rchallengeName\x18\x01 \x01(\tR\rchallengeName\"/\n\x1bSubmitEvidenceReportRequest\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"\x1e\n\x1cSubmitEvidenceReportResponse\"@\n\x0cLoginRequest\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\"G\n\rLoginResponse\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x1a\n\x08userRole\x18\x02 \x01(\tR\x08userRole\"\x84\x01\n\x08\x45vidence\x12\x0e\n\x02id\x18\x01 \x01(\rR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x63hallengeID\x18\x03 \x01(\rR\x0b\x63hallengeID\x12\x0c\n\x01x\x18\x04 \x01(\x05R\x01x\x12\x0c\n\x01y\x18\x05 \x01(\x05R\x01y\x12\x16\n\x06isFlag\x18\x06 \x01(\x08R\x06isFlag\"V\n\nConnection\x12\x0e\n\x02id\x18\x01 \x01(\rR\x02id\x12\x16\n\x06source\x18\x02 \x01(\rR\x06source\x12 \n\x0b\x64\x65stination\x18\x03 \x01(\rR\x0b\x64\x65stination\"\x1e\n\x1cGetDiscoveredEvidenceRequest\"\x97\x01\n\x1dGetDiscoveredEvidenceResponse\x12\x16\n\x06report\x18\x01 \x01(\tR\x06report\x12*\n\x08\x65vidence\x18\x02 \x03(\x0b\x32\x0e.xctf.EvidenceR\x08\x65vidence\x12\x32\n\x0b\x63onnections\x18\x03 \x03(\x0b\x32\x10.xctf.ConnectionR\x0b\x63onnections\"\x7f\n\x15SubmitEvidenceRequest\x12\x1a\n\x08\x65vidence\x18\x01 \x01(\tR\x08\x65vidence\x12\x0c\n\x01x\x18\x02 \x01(\x05R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x05R\x01y\x12\x16\n\x06isFlag\x18\x04 \x01(\x08R\x06isFlag\x12\x16\n\x06remove\x18\x05 \x01(\x08R\x06remove\",\n\x16SubmitEvidenceResponse\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"s\n\x1fSubmitEvidenceConnectionRequest\x12\x16\n\x06source\x18\x01 \x01(\rR\x06source\x12 \n\x0b\x64\x65stination\x18\x02 \x01(\rR\x0b\x64\x65stination\x12\x16\n\x06remove\x18\x03 \x01(\x08R\x06remove\"<\n SubmitEvidenceConnectionResponse\x12\x18\n\x07\x63reated\x18\x01 \x01(\x08R\x07\x63reated\"_\n\x0fRegisterRequest\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x14\n\x05\x65mail\x18\x02 \x01(\tR\x05\x65mail\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\",\n\x10RegisterResponse\x12\x18\n\x07\x63reated\x18\x01 \x01(\x08R\x07\x63reated\"L\n\x04Page\x12\x14\n\x05route\x18\x01 \x01(\tR\x05route\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\"\x14\n\x12\x43urrentUserRequest\"o\n\x13\x43urrentUserResponse\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x1a\n\x08userRole\x18\x02 \x01(\tR\x08userRole\x12 \n\x05pages\x18\x03 \x03(\x0b\x32\n.xctf.PageR\x05pages\"\'\n\x11SubmitFlagRequest\x12\x12\n\x04\x66lag\x18\x01 \x01(\tR\x04\x66lag\".\n\x12SubmitFlagResponse\x12\x18\n\x07\x63orrect\x18\x01 \x01(\x08R\x07\x63orrect\"v\n\x0cTeamProgress\x12\x1a\n\x08teamName\x18\x01 \x01(\tR\x08teamName\x12\x1e\n\nhasWriteup\x18\x02 \x01(\x08R\nhasWriteup\x12\x14\n\x05score\x18\x03 \x01(\rR\x05score\x12\x14\n\x05grade\x18\x04 \x01(\rR\x05grade\"\x19\n\x17GetTeamsProgressRequest\"D\n\x18GetTeamsProgressResponse\x12(\n\x05teams\x18\x01 \x03(\x0b\x32\x12.xctf.TeamProgressR\x05teams\"3\n\tChallenge\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x66lag\x18\x02 \x01(\tR\x04\x66lag\"\x19\n\x17GetAllChallengesRequest\"K\n\x18GetAllChallengesResponse\x12/\n\nchallenges\x18\x01 \x03(\x0b\x32\x0f.xctf.ChallengeR\nchallenges\".\n\x12SetHomePageRequest\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"\x14\n\x12GetHomePageRequest\"/\n\x13GetHomePageResponse\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"-\n\x15\x46orgotPasswordRequest\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\"0\n\x14SubmitWriteupRequest\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"/\n\x11GetWriteupRequest\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\".\n\x12GetWriteupResponse\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"F\n\x12SubmitGradeRequest\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x14\n\x05score\x18\x02 \x01(\rR\x05score\"\x81\x01\n\rHighlightArea\x12\x16\n\x06height\x18\x01 \x01(\x05R\x06height\x12\x14\n\x05width\x18\x02 \x01(\x05R\x05width\x12\x1c\n\tpageIndex\x18\x03 \x01(\rR\tpageIndex\x12\x10\n\x03top\x18\x04 \x01(\x05R\x03top\x12\x12\n\x04left\x18\x05 \x01(\x05R\x04left\"\x9e\x01\n\x15SubmitCommentsRequest\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x0e\n\x02id\x18\x02 \x01(\rR\x02id\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x12)\n\x05\x61reas\x18\x04 \x03(\x0b\x32\x13.xctf.HighlightAreaR\x05\x61reas\x12\x14\n\x05quote\x18\x05 \x01(\tR\x05quote\"1\n\x13GetUserGraphRequest\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\"v\n\x14GetUserGraphResponse\x12*\n\x08\x65vidence\x18\x01 \x03(\x0b\x32\x0e.xctf.EvidenceR\x08\x65vidence\x12\x32\n\x0b\x63onnections\x18\x02 \x03(\x0b\x32\x10.xctf.ConnectionR\x0b\x63onnections2\xd1\x06\n\x07\x42\x61\x63kend\x12\x39\n\x08Register\x12\x15.xctf.RegisterRequest\x1a\x16.xctf.RegisterResponse\x12\x30\n\x05Login\x12\x12.xctf.LoginRequest\x1a\x13.xctf.LoginResponse\x12\"\n\x06Logout\x12\x0b.xctf.Empty\x1a\x0b.xctf.Empty\x12\x42\n\x0b\x43urrentUser\x12\x18.xctf.CurrentUserRequest\x1a\x19.xctf.CurrentUserResponse\x12?\n\nSubmitFlag\x12\x17.xctf.SubmitFlagRequest\x1a\x18.xctf.SubmitFlagResponse\x12\\\n\x14SubmitEvidenceReport\x12!.xctf.SubmitEvidenceReportRequest\x1a!.xctf.SubmitEvidenceReportRequest\x12`\n\x15GetDiscoveredEvidence\x12\".xctf.GetDiscoveredEvidenceRequest\x1a#.xctf.GetDiscoveredEvidenceResponse\x12K\n\x0eSubmitEvidence\x12\x1b.xctf.SubmitEvidenceRequest\x1a\x1c.xctf.SubmitEvidenceResponse\x12i\n\x18SubmitEvidenceConnection\x12%.xctf.SubmitEvidenceConnectionRequest\x1a&.xctf.SubmitEvidenceConnectionResponse\x12\x42\n\x0bGetHomePage\x12\x18.xctf.GetHomePageRequest\x1a\x19.xctf.GetHomePageResponse\x12:\n\x0e\x46orgotPassword\x12\x1b.xctf.ForgotPasswordRequest\x1a\x0b.xctf.Empty\x12\x38\n\rSubmitWriteup\x12\x1a.xctf.SubmitWriteupRequest\x1a\x0b.xctf.Empty2\xd9\x04\n\x05\x41\x64min\x12<\n\x0fUpsertChallenge\x12\x1c.xctf.UpsertChallengeRequest\x1a\x0b.xctf.Empty\x12<\n\x0f\x44\x65leteChallenge\x12\x1c.xctf.DeleteChallengeRequest\x1a\x0b.xctf.Empty\x12Q\n\x10GetTeamsProgress\x12\x1d.xctf.GetTeamsProgressRequest\x1a\x1e.xctf.GetTeamsProgressResponse\x12Q\n\x10GetAllChallenges\x12\x1d.xctf.GetAllChallengesRequest\x1a\x1e.xctf.GetAllChallengesResponse\x12\x34\n\x0bSetHomePage\x12\x18.xctf.SetHomePageRequest\x1a\x0b.xctf.Empty\x12?\n\nGetWriteup\x12\x17.xctf.GetWriteupRequest\x1a\x18.xctf.GetWriteupResponse\x12\x34\n\x0bSubmitGrade\x12\x18.xctf.SubmitGradeRequest\x1a\x0b.xctf.Empty\x12:\n\x0eSubmitComments\x12\x1b.xctf.SubmitCommentsRequest\x1a\x0b.xctf.Empty\x12\x45\n\x0cGetUserGraph\x12\x19.xctf.GetUserGraphRequest\x1a\x1a.xctf.GetUserGraphResponseBg\n\x08\x63om.xctfB\tXctfProtoP\x01Z github.com/xctf-io/xctf/gen/xctf\xa2\x02\x03XXX\xaa\x02\x04Xctf\xca\x02\x04Xctf\xe2\x02\x10Xctf\\GPBMetadata\xea\x02\x04Xctfb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xctf.xctf_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\010com.xctfB\tXctfProtoP\001Z github.com/xctf-io/xctf/gen/xctf\242\002\003XXX\252\002\004Xctf\312\002\004Xctf\342\002\020Xctf\\GPBMetadata\352\002\004Xctf'
  _globals['_EMPTY']._serialized_start=25
  _globals['_EMPTY']._serialized_end=32
  _globals['_UPSERTCHALLENGEREQUEST']._serialized_start=34
  _globals['_UPSERTCHALLENGEREQUEST']._serialized_end=116
  _globals['_DELETECHALLENGEREQUEST']._serialized_start=118
  _globals['_DELETECHALLENGEREQUEST']._serialized_end=180
  _globals['_SUBMITEVIDENCEREPORTREQUEST']._serialized_start=182
  _globals['_SUBMITEVIDENCEREPORTREQUEST']._serialized_end=229
  _globals['_SUBMITEVIDENCEREPORTRESPONSE']._serialized_start=231
  _globals['_SUBMITEVIDENCEREPORTRESPONSE']._serialized_end=261
  _globals['_LOGINREQUEST']._serialized_start=263
  _globals['_LOGINREQUEST']._serialized_end=327
  _globals['_LOGINRESPONSE']._serialized_start=329
  _globals['_LOGINRESPONSE']._serialized_end=400
  _globals['_EVIDENCE']._serialized_start=403
  _globals['_EVIDENCE']._serialized_end=535
  _globals['_CONNECTION']._serialized_start=537
  _globals['_CONNECTION']._serialized_end=623
  _globals['_GETDISCOVEREDEVIDENCEREQUEST']._serialized_start=625
  _globals['_GETDISCOVEREDEVIDENCEREQUEST']._serialized_end=655
  _globals['_GETDISCOVEREDEVIDENCERESPONSE']._serialized_start=658
  _globals['_GETDISCOVEREDEVIDENCERESPONSE']._serialized_end=809
  _globals['_SUBMITEVIDENCEREQUEST']._serialized_start=811
  _globals['_SUBMITEVIDENCEREQUEST']._serialized_end=938
  _globals['_SUBMITEVIDENCERESPONSE']._serialized_start=940
  _globals['_SUBMITEVIDENCERESPONSE']._serialized_end=984
  _globals['_SUBMITEVIDENCECONNECTIONREQUEST']._serialized_start=986
  _globals['_SUBMITEVIDENCECONNECTIONREQUEST']._serialized_end=1101
  _globals['_SUBMITEVIDENCECONNECTIONRESPONSE']._serialized_start=1103
  _globals['_SUBMITEVIDENCECONNECTIONRESPONSE']._serialized_end=1163
  _globals['_REGISTERREQUEST']._serialized_start=1165
  _globals['_REGISTERREQUEST']._serialized_end=1260
  _globals['_REGISTERRESPONSE']._serialized_start=1262
  _globals['_REGISTERRESPONSE']._serialized_end=1306
  _globals['_PAGE']._serialized_start=1308
  _globals['_PAGE']._serialized_end=1384
  _globals['_CURRENTUSERREQUEST']._serialized_start=1386
  _globals['_CURRENTUSERREQUEST']._serialized_end=1406
  _globals['_CURRENTUSERRESPONSE']._serialized_start=1408
  _globals['_CURRENTUSERRESPONSE']._serialized_end=1519
  _globals['_SUBMITFLAGREQUEST']._serialized_start=1521
  _globals['_SUBMITFLAGREQUEST']._serialized_end=1560
  _globals['_SUBMITFLAGRESPONSE']._serialized_start=1562
  _globals['_SUBMITFLAGRESPONSE']._serialized_end=1608
  _globals['_TEAMPROGRESS']._serialized_start=1610
  _globals['_TEAMPROGRESS']._serialized_end=1728
  _globals['_GETTEAMSPROGRESSREQUEST']._serialized_start=1730
  _globals['_GETTEAMSPROGRESSREQUEST']._serialized_end=1755
  _globals['_GETTEAMSPROGRESSRESPONSE']._serialized_start=1757
  _globals['_GETTEAMSPROGRESSRESPONSE']._serialized_end=1825
  _globals['_CHALLENGE']._serialized_start=1827
  _globals['_CHALLENGE']._serialized_end=1878
  _globals['_GETALLCHALLENGESREQUEST']._serialized_start=1880
  _globals['_GETALLCHALLENGESREQUEST']._serialized_end=1905
  _globals['_GETALLCHALLENGESRESPONSE']._serialized_start=1907
  _globals['_GETALLCHALLENGESRESPONSE']._serialized_end=1982
  _globals['_SETHOMEPAGEREQUEST']._serialized_start=1984
  _globals['_SETHOMEPAGEREQUEST']._serialized_end=2030
  _globals['_GETHOMEPAGEREQUEST']._serialized_start=2032
  _globals['_GETHOMEPAGEREQUEST']._serialized_end=2052
  _globals['_GETHOMEPAGERESPONSE']._serialized_start=2054
  _globals['_GETHOMEPAGERESPONSE']._serialized_end=2101
  _globals['_FORGOTPASSWORDREQUEST']._serialized_start=2103
  _globals['_FORGOTPASSWORDREQUEST']._serialized_end=2148
  _globals['_SUBMITWRITEUPREQUEST']._serialized_start=2150
  _globals['_SUBMITWRITEUPREQUEST']._serialized_end=2198
  _globals['_GETWRITEUPREQUEST']._serialized_start=2200
  _globals['_GETWRITEUPREQUEST']._serialized_end=2247
  _globals['_GETWRITEUPRESPONSE']._serialized_start=2249
  _globals['_GETWRITEUPRESPONSE']._serialized_end=2295
  _globals['_SUBMITGRADEREQUEST']._serialized_start=2297
  _globals['_SUBMITGRADEREQUEST']._serialized_end=2367
  _globals['_HIGHLIGHTAREA']._serialized_start=2370
  _globals['_HIGHLIGHTAREA']._serialized_end=2499
  _globals['_SUBMITCOMMENTSREQUEST']._serialized_start=2502
  _globals['_SUBMITCOMMENTSREQUEST']._serialized_end=2660
  _globals['_GETUSERGRAPHREQUEST']._serialized_start=2662
  _globals['_GETUSERGRAPHREQUEST']._serialized_end=2711
  _globals['_GETUSERGRAPHRESPONSE']._serialized_start=2713
  _globals['_GETUSERGRAPHRESPONSE']._serialized_end=2831
  _globals['_BACKEND']._serialized_start=2834
  _globals['_BACKEND']._serialized_end=3683
  _globals['_ADMIN']._serialized_start=3686
  _globals['_ADMIN']._serialized_end=4287
# @@protoc_insertion_point(module_scope)
