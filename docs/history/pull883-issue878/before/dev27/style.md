(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ tox -e style27
style27 create: /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/style27
style27 installdeps: pycodestyle
style27 develop-inst: /home/cwm/git/bb.FLXSA/quant/arctic_878
style27 installed: DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.,-e git+https://github.com/c-w-m/arctic.git@42087e5abbeedeec36513888043eb28f82def841#egg=arctic,decorator==4.4.2,enum-compat==0.0.3,enum34==1.1.10,funcsigs==1.0.2,future==0.18.2,futures==3.3.0,lz4==2.2.1,mock==3.0.5,mockextras==1.0.2,numpy==1.16.6,pandas==0.24.2,pycodestyle==2.6.0,pymongo==3.11.2,python-dateutil==2.8.1,pytz==2020.5,six==1.15.0,tzlocal==2.1
style27 run-test-pre: PYTHONHASHSEED='1998019282'
style27 run-test: commands[0] | python -c 'print((80*"~")+"\ntestenv:style-python2.7\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
testenv:style-python2.7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
style27 run-test: commands[1] | pycodestyle arctic tests
tests/integration/test_arctic.py:105:48: E127 continuation line over-indented for visual indent
tests/integration/test_arctic.py:107:38: E127 continuation line over-indented for visual indent
tests/integration/test_arctic.py:114:44: E127 continuation line over-indented for visual indent
tests/integration/test_arctic.py:116:34: E127 continuation line over-indented for visual indent
tests/integration/test_arctic.py:127:48: E127 continuation line over-indented for visual indent
tests/integration/test_arctic.py:129:38: E127 continuation line over-indented for visual indent
tests/integration/test_arctic.py:187:5: E741 ambiguous variable name 'l'
tests/integration/test_arctic.py:190:5: E741 ambiguous variable name 'l'
tests/integration/test_arctic.py:193:9: E741 ambiguous variable name 'l'
tests/integration/test_arctic.py:200:5: E741 ambiguous variable name 'l'
tests/integration/test_arctic.py:208:5: E741 ambiguous variable name 'l'
tests/integration/test_arctic.py:212:9: E741 ambiguous variable name 'l'
tests/integration/test_arctic_multithreading.py:16:1: E302 expected 2 blank lines, found 1
tests/integration/test_decorators.py:6:34: E128 continuation line under-indented for visual indent
tests/integration/test_decorators.py:7:34: E128 continuation line under-indented for visual indent
tests/integration/test_howtos.py:9:59: W291 trailing whitespace
tests/integration/chunkstore/test_chunkstore.py:92:1: E302 expected 2 blank lines, found 1
tests/integration/chunkstore/test_chunkstore.py:312:62: E203 whitespace before ','
tests/integration/chunkstore/test_chunkstore.py:340:62: E203 whitespace before ','
tests/integration/chunkstore/test_chunkstore.py:395:62: E203 whitespace before ','
tests/integration/chunkstore/test_chunkstore.py:1085:46: E251 unexpected spaces around keyword / parameter equals
tests/integration/chunkstore/test_chunkstore.py:1085:48: E251 unexpected spaces around keyword / parameter equals
tests/integration/chunkstore/test_chunkstore.py:1094:46: E251 unexpected spaces around keyword / parameter equals
tests/integration/chunkstore/test_chunkstore.py:1094:48: E251 unexpected spaces around keyword / parameter equals
tests/integration/chunkstore/test_chunkstore.py:1114:49: E711 comparison to None should be 'if cond is None:'
tests/integration/chunkstore/test_chunkstore.py:1196:1: E302 expected 2 blank lines, found 1
tests/integration/chunkstore/test_fixes.py:20:1: E302 expected 2 blank lines, found 1
tests/integration/chunkstore/test_fixes.py:47:48: E226 missing whitespace around arithmetic operator
tests/integration/chunkstore/test_fixes.py:157:67: E231 missing whitespace after ','
tests/integration/chunkstore/test_fixes.py:157:71: E231 missing whitespace after ','
tests/integration/chunkstore/test_fixes.py:159:47: E231 missing whitespace after ','
tests/integration/chunkstore/test_fixes.py:159:49: E231 missing whitespace after ','
tests/integration/chunkstore/test_fixes.py:166:5: E303 too many blank lines (2)
tests/integration/chunkstore/test_fixes.py:174:47: E231 missing whitespace after ','
tests/integration/chunkstore/test_fixes.py:174:49: E231 missing whitespace after ','
tests/integration/chunkstore/test_utils.py:18:67: E226 missing whitespace around arithmetic operator
tests/integration/chunkstore/test_utils.py:19:48: E226 missing whitespace around arithmetic operator
tests/integration/chunkstore/test_utils.py:24:99: E226 missing whitespace around arithmetic operator
tests/integration/chunkstore/test_utils.py:24:107: E226 missing whitespace around arithmetic operator
tests/integration/chunkstore/tools/test_tools.py:17:48: E226 missing whitespace around arithmetic operator
tests/integration/tickstore/test_toplevel.py:17:1: E302 expected 2 blank lines, found 1
tests/integration/tickstore/test_toplevel.py:30:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:31:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:33:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:34:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:36:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:37:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:44:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:45:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:57:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:58:44: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_toplevel.py:210:127: W291 trailing whitespace
tests/integration/tickstore/test_toplevel.py:268:11: E225 missing whitespace around operator
tests/integration/tickstore/test_ts_delete.py:20:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_delete.py:52:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:21:19: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:33:18: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:54:19: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:66:18: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:83:19: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:95:18: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:111:114: W291 trailing whitespace
tests/integration/tickstore/test_ts_read.py:131:19: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:144:19: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:168:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:169:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:170:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:171:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:172:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:173:13: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:176:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:177:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:178:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:179:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:180:13: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:181:13: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:198:26: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:199:25: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:227:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:293:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:306:39: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:321:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:355:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:390:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:401:77: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:405:77: E127 continuation line over-indented for visual indent
tests/integration/tickstore/test_ts_read.py:444:20: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:445:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:446:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:447:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:448:18: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:450:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:451:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:452:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:453:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:459:20: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:460:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:461:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:462:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:463:18: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:465:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:466:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:467:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:468:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:485:16: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:486:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:487:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:488:16: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:489:14: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:491:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:492:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:493:16: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:494:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:500:20: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:501:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:502:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:503:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:504:18: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:506:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:507:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:508:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:509:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:529:16: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:530:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:531:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:532:16: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:533:14: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:535:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:536:16: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:537:16: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:538:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:544:20: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:545:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:546:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:547:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:548:18: E131 continuation line unaligned for hanging indent
tests/integration/tickstore/test_ts_read.py:550:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:551:20: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:552:20: E124 closing bracket does not match visual indentation
tests/integration/tickstore/test_ts_read.py:553:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:566:1: E302 expected 2 blank lines, found 1
tests/integration/tickstore/test_ts_read.py:572:20: E121 continuation line under-indented for hanging indent
tests/integration/tickstore/test_ts_read.py:574:20: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:575:19: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:590:16: E121 continuation line under-indented for hanging indent
tests/integration/tickstore/test_ts_read.py:592:16: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:593:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/tickstore/test_ts_read.py:597:38: E128 continuation line under-indented for visual indent
tests/integration/tickstore/test_ts_read.py:664:33: E261 at least two spaces before inline comment
tests/integration/tickstore/test_ts_read.py:666:7: E111 indentation is not a multiple of four
tests/integration/tickstore/test_ts_read.py:667:7: E111 indentation is not a multiple of four
tests/integration/tickstore/test_ts_read.py:669:7: E111 indentation is not a multiple of four
tests/integration/tickstore/test_ts_read.py:670:7: E111 indentation is not a multiple of four
tests/integration/tickstore/test_ts_read.py:681:63: E261 at least two spaces before inline comment
tests/integration/tickstore/test_ts_write.py:31:15: E123 closing bracket does not match indentation of opening bracket's line
tests/integration/store/test_metadata_store.py:36:23: E711 comparison to None should be 'if cond is None:'
tests/integration/store/test_metadata_store.py:67:33: E711 comparison to None should be 'if cond is None:'
tests/integration/store/test_ndarray_store_append.py:14:1: E302 expected 2 blank lines, found 1
tests/integration/store/test_pandas_store.py:104:61: E712 comparison to False should be 'if cond is False:' or 'if not cond:'
tests/integration/store/test_pandas_store.py:111:65: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:120:61: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:121:61: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:130:72: E128 continuation line under-indented for visual indent
tests/integration/store/test_pandas_store.py:131:72: E128 continuation line under-indented for visual indent
tests/integration/store/test_pandas_store.py:415:72: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:416:72: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:436:72: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:437:72: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:458:72: E127 continuation line over-indented for visual indent
tests/integration/store/test_pandas_store.py:459:72: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:71:1: E402 module level import not at top of file
tests/integration/store/test_version_store.py:72:1: E402 module level import not at top of file
tests/integration/store/test_version_store.py:73:1: E302 expected 2 blank lines, found 0
tests/integration/store/test_version_store.py:83:65: E712 comparison to False should be 'if cond is False:' or 'if not cond:'
tests/integration/store/test_version_store.py:143:9: E306 expected 1 blank line before a nested definition, found 0
tests/integration/store/test_version_store.py:148:70: E712 comparison to True should be 'if cond is True:' or 'if cond:'
tests/integration/store/test_version_store.py:158:35: E712 comparison to False should be 'if cond is False:' or 'if not cond:'
tests/integration/store/test_version_store.py:413:35: E712 comparison to True should be 'if cond is True:' or 'if cond:'
tests/integration/store/test_version_store.py:417:35: E712 comparison to False should be 'if cond is False:' or 'if not cond:'
tests/integration/store/test_version_store.py:976:37: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:981:37: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:987:37: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:994:37: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:1002:37: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:1011:37: E127 continuation line over-indented for visual indent
tests/integration/store/test_version_store.py:1109:33: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store.py:1109:58: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store.py:1140:76: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store.py:1195:27: E711 comparison to None should be 'if cond is None:'
tests/integration/store/test_version_store.py:1510:9: E306 expected 1 blank line before a nested definition, found 0
tests/integration/store/test_version_store.py:1534:9: E306 expected 1 blank line before a nested definition, found 0
tests/integration/store/test_version_store.py:1898:39: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store.py:1899:24: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store.py:1931:40: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store.py:1932:24: E226 missing whitespace around arithmetic operator
tests/integration/store/test_version_store_audit.py:147:26: E128 continuation line under-indented for visual indent
tests/integration/store/test_version_store_audit.py:153:26: E128 continuation line under-indented for visual indent
tests/integration/store/test_version_store_audit.py:158:33: E128 continuation line under-indented for visual indent
tests/integration/store/test_version_store_audit.py:159:26: E128 continuation line under-indented for visual indent
tests/integration/store/test_version_store_audit.py:189:43: E741 ambiguous variable name 'l'
tests/integration/store/test_version_store_audit.py:200:43: E741 ambiguous variable name 'l'
tests/integration/store/test_version_store_corruption.py:192:46: E262 inline comment should start with '# '
tests/integration/store/test_version_store_corruption.py:194:50: E262 inline comment should start with '# '
tests/integration/store/test_version_store_corruption.py:196:50: E262 inline comment should start with '# '
tests/integration/store/test_version_store_corruption.py:199:50: E262 inline comment should start with '# '
tests/integration/store/test_version_store_corruption.py:201:27: E261 at least two spaces before inline comment
tests/integration/store/test_version_store_corruption.py:201:28: E262 inline comment should start with '# '
tests/integration/store/test_version_store_corruption.py:256:5: E306 expected 1 blank line before a nested definition, found 0
tests/integration/scripts/test_copy_data.py:35:1: E302 expected 2 blank lines, found 1
tests/integration/scripts/test_delete_library.py:23:47: E127 continuation line over-indented for visual indent
tests/integration/scripts/test_delete_library.py:32:47: E127 continuation line over-indented for visual indent
tests/integration/scripts/test_delete_library.py:41:47: E127 continuation line over-indented for visual indent
tests/integration/scripts/test_delete_library.py:50:47: E127 continuation line over-indented for visual indent
tests/integration/scripts/test_delete_library.py:59:47: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:23:5: E125 continuation line with same indent as next logical line
tests/unit/test_arctic.py:24:13: E117 over-indented
tests/unit/test_arctic.py:70:13: E117 over-indented
tests/unit/test_arctic.py:95:13: E117 over-indented
tests/unit/test_arctic.py:118:17: E117 over-indented
tests/unit/test_arctic.py:119:42: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:120:42: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:135:13: E117 over-indented
tests/unit/test_arctic.py:136:34: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:137:34: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:245:78: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:248:78: E124 closing bracket does not match visual indentation
tests/unit/test_arctic.py:263:78: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:266:78: E124 closing bracket does not match visual indentation
tests/unit/test_arctic.py:280:78: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:283:78: E124 closing bracket does not match visual indentation
tests/unit/test_arctic.py:298:78: E127 continuation line over-indented for visual indent
tests/unit/test_arctic.py:301:78: E124 closing bracket does not match visual indentation
tests/unit/test_arctic.py:416:14: E225 missing whitespace around operator
tests/unit/test_arctic.py:465:17: E117 over-indented
tests/unit/test_compression.py:18:41: E226 missing whitespace around arithmetic operator
tests/unit/test_compression.py:19:48: E226 missing whitespace around arithmetic operator
tests/unit/test_decorators_unit.py:164:32: E124 closing bracket does not match visual indentation
tests/unit/test_decorators_unit.py:173:34: E128 continuation line under-indented for visual indent
tests/unit/test_decorators_unit.py:174:34: E128 continuation line under-indented for visual indent
tests/unit/test_decorators_unit.py:175:34: E124 closing bracket does not match visual indentation
tests/unit/test_multi_index.py:120:16: E225 missing whitespace around operator
tests/unit/test_multi_index.py:212:38: W291 trailing whitespace
tests/unit/date/test_daterange.py:11:17: E241 multiple spaces after ':'
tests/unit/date/test_daterange.py:13:23: E241 multiple spaces after ':'
tests/unit/date/test_daterange.py:15:22: E241 multiple spaces after ':'
tests/unit/date/test_daterange.py:21:19: E241 multiple spaces after ':'
tests/unit/date/test_daterange.py:23:19: E241 multiple spaces after ':'
tests/unit/date/test_daterange.py:25:17: E241 multiple spaces after ':'
tests/unit/date/test_daterange.py:55:1: E302 expected 2 blank lines, found 1
tests/unit/date/test_daterange.py:194:16: E128 continuation line under-indented for visual indent
tests/unit/date/test_daterange.py:198:73: E203 whitespace before ','
tests/unit/date/test_daterange.py:200:41: E203 whitespace before ','
tests/unit/date/test_daterange.py:200:48: E203 whitespace before ','
tests/unit/date/test_daterange.py:201:1: E302 expected 2 blank lines, found 0
tests/unit/date/test_util.py:18:29: E123 closing bracket does not match indentation of opening bracket's line
tests/unit/date/test_util.py:19:1: E124 closing bracket does not match visual indentation
tests/unit/date/test_util.py:109:16: E711 comparison to None should be 'if cond is None:'
tests/unit/date/test_util.py:119:23: E712 comparison to False should be 'if cond is False:' or 'if not cond:'
tests/unit/tickstore/test_tickstore.py:22:52: E203 whitespace before ':'
tests/unit/tickstore/test_tickstore.py:22:60: E203 whitespace before ','
tests/unit/tickstore/test_tickstore.py:34:6: E121 continuation line under-indented for hanging indent
tests/unit/tickstore/test_tickstore.py:34:82: E203 whitespace before ':'
tests/unit/tickstore/test_tickstore.py:34:90: E203 whitespace before ','
tests/unit/tickstore/test_tickstore.py:95:36: E226 missing whitespace around arithmetic operator
tests/unit/tickstore/test_tickstore.py:160:36: E226 missing whitespace around arithmetic operator
tests/unit/tickstore/test_toplevel.py:3:8: W291 trailing whitespace
tests/unit/store/test_metadata_store.py:33:42: E241 multiple spaces after ':'
tests/unit/store/test_metadata_store.py:49:42: E241 multiple spaces after ':'
tests/unit/store/test_metadata_store.py:65:42: E241 multiple spaces after ':'
tests/unit/store/test_metadata_store.py:82:42: E241 multiple spaces after ':'
tests/unit/store/test_metadata_store.py:99:42: E241 multiple spaces after ':'
tests/unit/store/test_ndarray_store.py:82:40: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:83:39: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:101:24: E128 continuation line under-indented for visual indent
tests/unit/store/test_ndarray_store.py:104:40: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:105:39: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:129:40: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:130:39: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:135:68: E203 whitespace before ':'
tests/unit/store/test_ndarray_store.py:139:98: E261 at least two spaces before inline comment
tests/unit/store/test_version_store.py:97:24: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:101:95: W291 trailing whitespace
tests/unit/store/test_version_store.py:113:24: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:118:64: W291 trailing whitespace
tests/unit/store/test_version_store.py:126:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:131:46: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:137:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:142:46: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:148:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:152:58: E127 continuation line over-indented for visual indent
tests/unit/store/test_version_store.py:158:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:159:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:160:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:161:22: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:188:64: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:227:82: W291 trailing whitespace
tests/unit/store/test_version_store.py:254:40: E127 continuation line over-indented for visual indent
tests/unit/store/test_version_store.py:255:40: E127 continuation line over-indented for visual indent
tests/unit/store/test_version_store.py:262:49: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:262:116: W291 trailing whitespace
tests/unit/store/test_version_store.py:263:49: E127 continuation line over-indented for visual indent
tests/unit/store/test_version_store.py:264:49: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:418:71: E226 missing whitespace around arithmetic operator
tests/unit/store/test_version_store.py:467:48: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store.py:541:122: E226 missing whitespace around arithmetic operator
tests/unit/store/test_version_store.py:561:122: E226 missing whitespace around arithmetic operator
tests/unit/store/test_version_store.py:575:1: E302 expected 2 blank lines, found 1
tests/unit/store/test_version_store.py:581:122: E226 missing whitespace around arithmetic operator
tests/unit/store/test_version_store_audit.py:59:37: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store_audit.py:104:36: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store_audit.py:105:36: E124 closing bracket does not match visual indentation
tests/unit/store/test_version_store_audit.py:112:47: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store_audit.py:122:36: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store_audit.py:123:36: E124 closing bracket does not match visual indentation
tests/unit/store/test_version_store_audit.py:130:47: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store_audit.py:188:134: W291 trailing whitespace
tests/unit/store/test_version_store_audit.py:190:36: E128 continuation line under-indented for visual indent
tests/unit/store/test_version_store_audit.py:213:69: W291 trailing whitespace
tests/unit/scripts/test_arctic_fsck.py:16:51: E127 continuation line over-indented for visual indent
tests/unit/scripts/test_arctic_fsck.py:17:51: E127 continuation line over-indented for visual indent
tests/unit/scripts/test_arctic_fsck.py:19:51: E127 continuation line over-indented for visual indent
tests/unit/scripts/test_arctic_fsck.py:20:51: E127 continuation line over-indented for visual indent
tests/unit/scripts/test_arctic_fsck.py:22:84: E127 continuation line over-indented for visual indent
tests/unit/scripts/test_arctic_fsck.py:35:84: E127 continuation line over-indented for visual indent
tests/unit/scripts/test_utils.py:32:15: E128 continuation line under-indented for visual indent
tests/unit/scripts/test_utils.py:48:15: E128 continuation line under-indented for visual indent
tests/unit/scripts/test_utils.py:62:15: E128 continuation line under-indented for visual indent
tests/unit/scripts/test_utils.py:76:15: E128 continuation line under-indented for visual indent
tests/unit/scripts/test_utils.py:91:9: E125 continuation line with same indent as next logical line
tests/unit/serialization/test_incremental.py:124:112: E226 missing whitespace around arithmetic operator
tests/unit/serialization/test_incremental.py:125:112: E226 missing whitespace around arithmetic operator
ERROR: InvocationError for command /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/style27/bin/pycodestyle arctic tests (exited with code 1)
_______________________________________________________________________________________________ summary ________________________________________________________________________________________________
ERROR:   style27: commands failed
(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$
