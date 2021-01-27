```shell
$ source ~/virtualenv/python3.7/bin/activate0.00s0.13s0.09s0.07s
...
================================================================================
=================================== FAILURES ===================================
__________________________________ test_quota __________________________________
arctic = <Arctic at 0x7fa62c05f4e0, connected to MongoClient(host=['127.12.101.44:26528'], document_class=dict, tz_aware=False, connect=True)>
library = <VersionStore at 0x7fa62c077048>
    <ArcticLibrary at 0x7fa62c077828, arctic_test.TEST>
        <Arctic at 0x7fa62c05f4e0, connected to MongoClient(host=['127.12.101.44:26528'], document_class=dict, tz_aware=False, connect=True)>
library_name = 'test.TEST'
    def test_quota(arctic, library, library_name):
        thing = list(range(100))
        library._arctic_lib.set_quota(10)
        assert arctic.get_quota(library_name) == 10
        assert library._arctic_lib.get_quota() == 10
>       library.write('thing', thing)
tests/integration/test_arctic.py:162: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [0, 1, 2, 3, 4, 5, ...]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________________________ test_lib_rename ________________________________
arctic = <Arctic at 0x7fa62c766da0, connected to MongoClient(host=['127.12.101.44:31920'], document_class=dict, tz_aware=False, connect=True)>
    def test_lib_rename(arctic):
        arctic.initialize_library('test')
        l = arctic['test']
>       l.write('test_data', 'abc')
tests/integration/test_arctic.py:188: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'abc'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_lib_rename_namespace ___________________________
arctic = <Arctic at 0x7fa62d874e80, connected to MongoClient(host=['127.12.101.44:27885'], document_class=dict, tz_aware=False, connect=True)>
    def test_lib_rename_namespace(arctic):
        arctic.initialize_library('namespace.test')
        l = arctic['namespace.test']
>       l.write('test_data', 'abc')
tests/integration/test_arctic.py:201: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'abc'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________________________ test_multiprocessing_safety __________________________
mongo_host = '127.12.101.44:1580', library_name = 'test.TEST'
    @pytest.mark.timeout(600)
    def test_multiprocessing_safety(mongo_host, library_name):
        # Create/initialize library at the parent process, then spawn children, and start them aligned in time
        total_processes = 64
        total_writes_per_child = 100
    
        register_get_auth_hook(my_auth_hook)
    
        global MY_ARCTIC
        MY_ARCTIC = Arctic(mongo_host=mongo_host)
    
        MY_ARCTIC.initialize_library(library_name, VERSION_STORE)
        assert isinstance(MY_ARCTIC.get_library(library_name), VersionStore)
    
        processes = [Process(target=f, args=(library_name, total_writes_per_child, True)) for _ in range(total_processes)]
    
        for p in processes:
            p.start()
    
        for p in processes:
            p.join()
    
        for p in processes:
>           assert p.exitcode == 0
E           assert 1 == 0
E             +1
E             -0
tests/integration/test_arctic_multithreading.py:69: AssertionError

================================================================================

_______________ test_multiprocessing_safety_parent_children_race _______________
mongo_host = '127.12.101.44:6617', library_name = 'test.TEST'
    @pytest.mark.timeout(600)
    def test_multiprocessing_safety_parent_children_race(mongo_host, library_name):
        # Create Arctic and directly fork/start children (no wait)
        total_iterations = 12
        total_processes = 6
        total_writes_per_child = 20
    
        global MY_ARCTIC
    
        for i in range(total_iterations):
            processes = list()
    
            MY_ARCTIC = Arctic(mongo_host=mongo_host)
            for j in range(total_processes):
                p = Process(target=f, args=(library_name, total_writes_per_child, False))
                p.start()  # start directly, don't wait to create first all children procs
                processes.append(p)
    
            MY_ARCTIC.initialize_library(library_name, VERSION_STORE)  # this will unblock spinning children
    
            for p in processes:
                p.join()
    
            for p in processes:
>               assert p.exitcode == 0
E               assert 1 == 0
E                 +1
E                 -0
tests/integration/test_arctic_multithreading.py:98: AssertionError

================================================================================

_______________________ test_howto[how_to_use_arctic.py] _______________________
howto = 'how_to_use_arctic.py', mongo_host = '127.12.101.44:24393'
    @pytest.mark.parametrize('howto', sorted([x.split('/')[-1]
                                              for x in glob.glob(os.path.join(HOWTO_DIR, 'how_to_*.py'))]))
    def test_howto(howto, mongo_host):
>       exec(open(HOWTO_DIR + "/" + howto).read(), {'mongo_host': mongo_host})
tests/integration/test_howtos.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
<string>:41: in <module>
    ???
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_cleanup_orphaned_chunks[True-data0-FwPointersCfg.DISABLED] ________
mongo_host = '127.12.101.44:29523'
library = <VersionStore at 0x7fa61d857630>
    <ArcticLibrary at 0x7fa61d857be0, arctic_user.library>
        <Arctic at 0x7fa61d80ce80, connected to MongoClient(host=['127.12.101.44:29523'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_cleanup_orphaned_chunks[True-data1-FwPointersCfg.HYBRID] _________
mongo_host = '127.12.101.44:23436'
library = <VersionStore at 0x7fa61d8cc240>
    <ArcticLibrary at 0x7fa61d8866d8, arctic_user.library>
        <Arctic at 0x7fa61d86fba8, connected to MongoClient(host=['127.12.101.44:23436'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_cleanup_orphaned_chunks[True-data2-FwPointersCfg.ENABLED] ________
mongo_host = '127.12.101.44:13773'
library = <VersionStore at 0x7fa61d9249b0>
    <ArcticLibrary at 0x7fa61d924240, arctic_user.library>
        <Arctic at 0x7fa61d86f048, connected to MongoClient(host=['127.12.101.44:13773'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_cleanup_orphaned_chunks[False-data6-FwPointersCfg.DISABLED] _______
mongo_host = '127.12.101.44:30642'
library = <VersionStore at 0x7fa61d8cc710>
    <ArcticLibrary at 0x7fa61d8cc7b8, arctic_user.library>
        <Arctic at 0x7fa61e776748, connected to MongoClient(host=['127.12.101.44:30642'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_cleanup_orphaned_chunks[False-data7-FwPointersCfg.HYBRID] ________
mongo_host = '127.12.101.44:16293'
library = <VersionStore at 0x7fa62c85ea58>
    <ArcticLibrary at 0x7fa61e6a0cf8, arctic_user.library>
        <Arctic at 0x7fa630b8fdd8, connected to MongoClient(host=['127.12.101.44:16293'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_cleanup_orphaned_chunks[False-data8-FwPointersCfg.ENABLED] ________
mongo_host = '127.12.101.44:30096'
library = <VersionStore at 0x7fa61e7ce208>
    <ArcticLibrary at 0x7fa61e7ce400, arctic_user.library>
        <Arctic at 0x7fa61e7dbc88, connected to MongoClient(host=['127.12.101.44:30096'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_____________ test_cleanup_noop[True-data0-FwPointersCfg.DISABLED] _____________
mongo_host = '127.12.101.44:13358'
library = <VersionStore at 0x7fa61e684860>
    <ArcticLibrary at 0x7fa61e684128, arctic_user.library>
        <Arctic at 0x7fa61e684908, connected to MongoClient(host=['127.12.101.44:13358'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


______________ test_cleanup_noop[True-data1-FwPointersCfg.HYBRID] ______________
mongo_host = '127.12.101.44:14923'
library = <VersionStore at 0x7fa61d815240>
    <ArcticLibrary at 0x7fa61d815be0, arctic_user.library>
        <Arctic at 0x7fa61d8ad6a0, connected to MongoClient(host=['127.12.101.44:14923'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_____________ test_cleanup_noop[True-data2-FwPointersCfg.ENABLED] ______________
mongo_host = '127.12.101.44:27698'
library = <VersionStore at 0x7fa61e7ed240>
    <ArcticLibrary at 0x7fa61e7ed9e8, arctic_user.library>
        <Arctic at 0x7fa61e68dcc0, connected to MongoClient(host=['127.12.101.44:27698'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


____________ test_cleanup_noop[False-data6-FwPointersCfg.DISABLED] _____________
mongo_host = '127.12.101.44:17611'
library = <VersionStore at 0x7fa61e5a0be0>
    <ArcticLibrary at 0x7fa61e5a0048, arctic_user.library>
        <Arctic at 0x7fa61e5a0080, connected to MongoClient(host=['127.12.101.44:17611'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_____________ test_cleanup_noop[False-data7-FwPointersCfg.HYBRID] ______________
mongo_host = '127.12.101.44:18258'
library = <VersionStore at 0x7fa61e69e400>
    <ArcticLibrary at 0x7fa61e69e128, arctic_user.library>
        <Arctic at 0x7fa62cc7fe48, connected to MongoClient(host=['127.12.101.44:18258'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_____________ test_cleanup_noop[False-data8-FwPointersCfg.ENABLED] _____________
mongo_host = '127.12.101.44:18083'
library = <VersionStore at 0x7fa61e67ec88>
    <ArcticLibrary at 0x7fa61e67ef28, arctic_user.library>
        <Arctic at 0x7fa61e67e198, connected to MongoClient(host=['127.12.101.44:18083'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_ test_cleanup_orphaned_chunks_ignores_recent[True-data0-FwPointersCfg.DISABLED] _
mongo_host = '127.12.101.44:24946'
library = <VersionStore at 0x7fa61e5a0828>
    <ArcticLibrary at 0x7fa61e5a0550, arctic_user.library>
        <Arctic at 0x7fa61e5f6ba8, connected to MongoClient(host=['127.12.101.44:24946'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        We don't cleanup any chunks in the range of today.  That's just asking for trouble
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(hours=12)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_ test_cleanup_orphaned_chunks_ignores_recent[True-data1-FwPointersCfg.HYBRID] _
mongo_host = '127.12.101.44:14285'
library = <VersionStore at 0x7fa61def19e8>
    <ArcticLibrary at 0x7fa61def1dd8, arctic_user.library>
        <Arctic at 0x7fa61e5a01d0, connected to MongoClient(host=['127.12.101.44:14285'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        We don't cleanup any chunks in the range of today.  That's just asking for trouble
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(hours=12)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunks_ignores_recent[True-data2-FwPointersCfg.ENABLED] _
mongo_host = '127.12.101.44:24438'
library = <VersionStore at 0x7fa61e7cfda0>
    <ArcticLibrary at 0x7fa61e7cf898, arctic_user.library>
        <Arctic at 0x7fa61e7cf780, connected to MongoClient(host=['127.12.101.44:24438'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        We don't cleanup any chunks in the range of today.  That's just asking for trouble
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(hours=12)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================


_ test_cleanup_orphaned_chunks_ignores_recent[False-data6-FwPointersCfg.DISABLED] _
mongo_host = '127.12.101.44:19246'
library = <VersionStore at 0x7fa61e7ed320>
    <ArcticLibrary at 0x7fa61d8cb6d8, arctic_user.library>
        <Arctic at 0x7fa61d8575f8, connected to MongoClient(host=['127.12.101.44:19246'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        We don't cleanup any chunks in the range of today.  That's just asking for trouble
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(hours=12)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunks_ignores_recent[False-data7-FwPointersCfg.HYBRID] _
mongo_host = '127.12.101.44:11055'
library = <VersionStore at 0x7fa61e70bda0>
    <ArcticLibrary at 0x7fa61e70b128, arctic_user.library>
        <Arctic at 0x7fa61dbeb898, connected to MongoClient(host=['127.12.101.44:11055'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        We don't cleanup any chunks in the range of today.  That's just asking for trouble
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(hours=12)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunks_ignores_recent[False-data8-FwPointersCfg.ENABLED] _
mongo_host = '127.12.101.44:8869'
library = <VersionStore at 0x7fa61e6eb7f0>
    <ArcticLibrary at 0x7fa61e6ebf98, arctic_user.library>
        <Arctic at 0x7fa61e595550, connected to MongoClient(host=['127.12.101.44:8869'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        We don't cleanup any chunks in the range of today.  That's just asking for trouble
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(hours=12)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunk_doesnt_break_versions[data0-FwPointersCfg.DISABLED] _
mongo_host = '127.12.101.44:27558'
library = <VersionStore at 0x7fa61e5efc18>
    <ArcticLibrary at 0x7fa61e5efcc0, arctic_user.library>
        <Arctic at 0x7fa61e5efb70, connected to MongoClient(host=['127.12.101.44:27558'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('data, fw_pointers_config',
                             [(x, y) for (x, y) in itertools.product(
                                 [some_object, ts],
                                 [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
        """
        Check that a chunk pointed to by more than one version, aren't inadvertently cleared
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunk_doesnt_break_versions[data1-FwPointersCfg.HYBRID] _
mongo_host = '127.12.101.44:21197'
library = <VersionStore at 0x7fa61e793470>
    <ArcticLibrary at 0x7fa61e793d30, arctic_user.library>
        <Arctic at 0x7fa61e5c35c0, connected to MongoClient(host=['127.12.101.44:21197'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('data, fw_pointers_config',
                             [(x, y) for (x, y) in itertools.product(
                                 [some_object, ts],
                                 [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
        """
        Check that a chunk pointed to by more than one version, aren't inadvertently cleared
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunk_doesnt_break_versions[data2-FwPointersCfg.ENABLED] _
mongo_host = '127.12.101.44:24011'
library = <VersionStore at 0x7fa61e5a0c50>
    <ArcticLibrary at 0x7fa61e5a0fd0, arctic_user.library>
        <Arctic at 0x7fa61e5a0198, connected to MongoClient(host=['127.12.101.44:24011'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('data, fw_pointers_config',
                             [(x, y) for (x, y) in itertools.product(
                                 [some_object, ts],
                                 [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
        """
        Check that a chunk pointed to by more than one version, aren't inadvertently cleared
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
>               library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunk_doesnt_break_versions[data3-FwPointersCfg.DISABLED] _
mongo_host = '127.12.101.44:9488'
library = <VersionStore at 0x7fa61e5d31d0>
    <ArcticLibrary at 0x7fa61e5d3c88, arctic_user.library>
        <Arctic at 0x7fa61e5d39b0, connected to MongoClient(host=['127.12.101.44:9488'], document_class=dict, tz_aware=False, connect=True)>
data =                          near
times                        
2012-09-08 17:06:11.040   1.0
2012-10-08 17:06:11.040   2.0
2012-10-09 17:06:11.040   2.5
2012-11-08 17:06:11.040   3.0
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('data, fw_pointers_config',
                             [(x, y) for (x, y) in itertools.product(
                                 [some_object, ts],
                                 [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
        """
        Check that a chunk pointed to by more than one version, aren't inadvertently cleared
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
                library.write('symbol', data, prune_previous_version=False)
    
            # Re-Write the data again
            # Write a whole new version rather than going down the append path...
            #     - we want two self-standing versions, the removal of one shouldn't break the other...
            with patch('arctic.store._ndarray_store._APPEND_COUNT', 0):
                library.write('symbol', data, prune_previous_version=False)
            library._delete_version('symbol', 1)
            library._collection.versions.delete_one({'_id': _id})
            assert repr(library.read('symbol').data) == repr(data)
    
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert repr(library.read('symbol').data) == repr(data)
>           library.delete('symbol')
tests/integration/scripts/test_arctic_fsck.py:133: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunk_doesnt_break_versions[data4-FwPointersCfg.HYBRID] _
mongo_host = '127.12.101.44:20951'
library = <VersionStore at 0x7fa61e75ce10>
    <ArcticLibrary at 0x7fa61e7dd518, arctic_user.library>
        <Arctic at 0x7fa61e75ccf8, connected to MongoClient(host=['127.12.101.44:20951'], document_class=dict, tz_aware=False, connect=True)>
data =                          near
times                        
2012-09-08 17:06:11.040   1.0
2012-10-08 17:06:11.040   2.0
2012-10-09 17:06:11.040   2.5
2012-11-08 17:06:11.040   3.0
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('data, fw_pointers_config',
                             [(x, y) for (x, y) in itertools.product(
                                 [some_object, ts],
                                 [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
        """
        Check that a chunk pointed to by more than one version, aren't inadvertently cleared
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
                library.write('symbol', data, prune_previous_version=False)
    
            # Re-Write the data again
            # Write a whole new version rather than going down the append path...
            #     - we want two self-standing versions, the removal of one shouldn't break the other...
            with patch('arctic.store._ndarray_store._APPEND_COUNT', 0):
                library.write('symbol', data, prune_previous_version=False)
            library._delete_version('symbol', 1)
            library._collection.versions.delete_one({'_id': _id})
            assert repr(library.read('symbol').data) == repr(data)
    
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert repr(library.read('symbol').data) == repr(data)
>           library.delete('symbol')
tests/integration/scripts/test_arctic_fsck.py:133: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_cleanup_orphaned_chunk_doesnt_break_versions[data5-FwPointersCfg.ENABLED] _
mongo_host = '127.12.101.44:14065'
library = <VersionStore at 0x7fa61e57d898>
    <ArcticLibrary at 0x7fa61e57d630, arctic_user.library>
        <Arctic at 0x7fa61e57de80, connected to MongoClient(host=['127.12.101.44:14065'], document_class=dict, tz_aware=False, connect=True)>
data =                          near
times                        
2012-09-08 17:06:11.040   1.0
2012-10-08 17:06:11.040   2.0
2012-10-09 17:06:11.040   2.5
2012-11-08 17:06:11.040   3.0
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('data, fw_pointers_config',
                             [(x, y) for (x, y) in itertools.product(
                                 [some_object, ts],
                                 [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
        """
        Check that a chunk pointed to by more than one version, aren't inadvertently cleared
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
            with patch("bson.ObjectId", return_value=_id):
                library.write('symbol', data, prune_previous_version=False)
    
            # Re-Write the data again
            # Write a whole new version rather than going down the append path...
            #     - we want two self-standing versions, the removal of one shouldn't break the other...
            with patch('arctic.store._ndarray_store._APPEND_COUNT', 0):
                library.write('symbol', data, prune_previous_version=False)
            library._delete_version('symbol', 1)
            library._collection.versions.delete_one({'_id': _id})
            assert repr(library.read('symbol').data) == repr(data)
    
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert repr(library.read('symbol').data) == repr(data)
>           library.delete('symbol')
tests/integration/scripts/test_arctic_fsck.py:133: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_cleanup_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] ______
mongo_host = '127.12.101.44:23799'
library = <VersionStore at 0x7fa61e767ac8>
    <ArcticLibrary at 0x7fa61e767cf8, arctic_user.library>
        <Arctic at 0x7fa61e5ccc18, connected to MongoClient(host=['127.12.101.44:23799'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_cleanup_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] _______
mongo_host = '127.12.101.44:12563'
library = <VersionStore at 0x7fa61e5ef1d0>
    <ArcticLibrary at 0x7fa61e5ef358, arctic_user.library>
        <Arctic at 0x7fa61e5ef908, connected to MongoClient(host=['127.12.101.44:12563'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_cleanup_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] _______
mongo_host = '127.12.101.44:5191'
library = <VersionStore at 0x7fa61e7db748>
    <ArcticLibrary at 0x7fa61e7db4e0, arctic_user.library>
        <Arctic at 0x7fa61e7dbeb8, connected to MongoClient(host=['127.12.101.44:5191'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_cleanup_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] ______
mongo_host = '127.12.101.44:21693'
library = <VersionStore at 0x7fa61e5cc550>
    <ArcticLibrary at 0x7fa61d88a8d0, arctic_user.library>
        <Arctic at 0x7fa61e57de10, connected to MongoClient(host=['127.12.101.44:21693'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_cleanup_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] _______
mongo_host = '127.12.101.44:23461'
library = <VersionStore at 0x7fa61e7d7588>
    <ArcticLibrary at 0x7fa61e7d7668, arctic_user.library>
        <Arctic at 0x7fa61e7a4ef0, connected to MongoClient(host=['127.12.101.44:23461'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_cleanup_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] ______
mongo_host = '127.12.101.44:18354'
library = <VersionStore at 0x7fa61e67eb70>
    <ArcticLibrary at 0x7fa61e67ec88, arctic_user.library>
        <Arctic at 0x7fa61e5e42b0, connected to MongoClient(host=['127.12.101.44:18354'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_cleanup_orphaned_snapshots_nop[True-data0-FwPointersCfg.DISABLED] ____
mongo_host = '127.12.101.44:25965'
library = <VersionStore at 0x7fa61e78da58>
    <ArcticLibrary at 0x7fa61e78d1d0, arctic_user.library>
        <Arctic at 0x7fa61e78d390, connected to MongoClient(host=['127.12.101.44:25965'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:184: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_cleanup_orphaned_snapshots_nop[True-data1-FwPointersCfg.HYBRID] _____
mongo_host = '127.12.101.44:19384'
library = <VersionStore at 0x7fa61e5cdb00>
    <ArcticLibrary at 0x7fa61e5cd080, arctic_user.library>
        <Arctic at 0x7fa61d86c9e8, connected to MongoClient(host=['127.12.101.44:19384'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:184: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_cleanup_orphaned_snapshots_nop[True-data2-FwPointersCfg.ENABLED] _____
mongo_host = '127.12.101.44:11100'
library = <VersionStore at 0x7fa61e58fbe0>
    <ArcticLibrary at 0x7fa61e58fb70, arctic_user.library>
        <Arctic at 0x7fa61e58ff98, connected to MongoClient(host=['127.12.101.44:11100'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:184: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___ test_cleanup_orphaned_snapshots_nop[False-data6-FwPointersCfg.DISABLED] ____
mongo_host = '127.12.101.44:26481'
library = <VersionStore at 0x7fa630d7b208>
    <ArcticLibrary at 0x7fa630d7b358, arctic_user.library>
        <Arctic at 0x7fa61e7ce898, connected to MongoClient(host=['127.12.101.44:26481'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:184: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_cleanup_orphaned_snapshots_nop[False-data7-FwPointersCfg.HYBRID] _____
mongo_host = '127.12.101.44:8102'
library = <VersionStore at 0x7fa61e699668>
    <ArcticLibrary at 0x7fa61e699160, arctic_user.library>
        <Arctic at 0x7fa61e706c50, connected to MongoClient(host=['127.12.101.44:8102'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:184: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_cleanup_orphaned_snapshots_nop[False-data8-FwPointersCfg.ENABLED] ____
mongo_host = '127.12.101.44:25712'
library = <VersionStore at 0x7fa61e79e748>
    <ArcticLibrary at 0x7fa61e79e710, arctic_user.library>
        <Arctic at 0x7fa61e79e9e8, connected to MongoClient(host=['127.12.101.44:25712'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            yesterday = dt.utcnow() - dtd(days=1, seconds=1)
            _id = bson.ObjectId.from_datetime(yesterday)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:184: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_dont_cleanup_recent_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] _
mongo_host = '127.12.101.44:1123'
library = <VersionStore at 0x7fa61e6a0198>
    <ArcticLibrary at 0x7fa61e5c32b0, arctic_user.library>
        <Arctic at 0x7fa61e5c3f98, connected to MongoClient(host=['127.12.101.44:1123'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            today = dt.utcnow() - dtd(hours=12, seconds=1)
            _id = bson.ObjectId.from_datetime(today)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_dont_cleanup_recent_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] _
mongo_host = '127.12.101.44:4486'
library = <VersionStore at 0x7fa61e75dbe0>
    <ArcticLibrary at 0x7fa61e75de10, arctic_user.library>
        <Arctic at 0x7fa61e75d518, connected to MongoClient(host=['127.12.101.44:4486'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            today = dt.utcnow() - dtd(hours=12, seconds=1)
            _id = bson.ObjectId.from_datetime(today)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_dont_cleanup_recent_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] _
mongo_host = '127.12.101.44:16523'
library = <VersionStore at 0x7fa61e58e908>
    <ArcticLibrary at 0x7fa61e58ec88, arctic_user.library>
        <Arctic at 0x7fa61d857048, connected to MongoClient(host=['127.12.101.44:16523'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = True
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            today = dt.utcnow() - dtd(hours=12, seconds=1)
            _id = bson.ObjectId.from_datetime(today)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_dont_cleanup_recent_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] _
mongo_host = '127.12.101.44:20586'
library = <VersionStore at 0x7fa61e77fe48>
    <ArcticLibrary at 0x7fa61e684ba8, arctic_user.library>
        <Arctic at 0x7fa61e582cc0, connected to MongoClient(host=['127.12.101.44:20586'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            today = dt.utcnow() - dtd(hours=12, seconds=1)
            _id = bson.ObjectId.from_datetime(today)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_dont_cleanup_recent_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] _
mongo_host = '127.12.101.44:6042'
library = <VersionStore at 0x7fa61e5bdeb8>
    <ArcticLibrary at 0x7fa61e5bdfd0, arctic_user.library>
        <Arctic at 0x7fa61e5bd828, connected to MongoClient(host=['127.12.101.44:6042'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            today = dt.utcnow() - dtd(hours=12, seconds=1)
            _id = bson.ObjectId.from_datetime(today)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_ test_dont_cleanup_recent_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] _
mongo_host = '127.12.101.44:22897'
library = <VersionStore at 0x7fa61e519a58>
    <ArcticLibrary at 0x7fa61e519390, arctic_user.library>
        <Arctic at 0x7fa61e519dd8, connected to MongoClient(host=['127.12.101.44:22897'], document_class=dict, tz_aware=False, connect=True)>
data = {'thing': sentinel.val}, dry_run = False
fw_pointers_config = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize(
        ['dry_run', 'data', 'fw_pointers_config'],
        [(x, y, z) for (x, y, z) in itertools.product(
            [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
    def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
        """
        Check that we do / don't cleanup chunks based on the dry-run
        """
        with FwPointersCtx(fw_pointers_config):
            today = dt.utcnow() - dtd(hours=12, seconds=1)
            _id = bson.ObjectId.from_datetime(today)
>           library.write('symbol', data, prune_previous_version=False)
tests/integration/scripts/test_arctic_fsck.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'thing': sentinel.val}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________________________ test_init_library _______________________________
mongo_host = '127.12.101.44:20853'
    def test_init_library(mongo_host):
        # Create the user agains the current mongo database
        with patch('arctic.scripts.arctic_init_library.do_db_auth', return_value=True), \
             patch('pymongo.database.Database.authenticate', return_value=True):
            run_as_main(mil.main, '--host', mongo_host, '--library', 'arctic_user.library')
    
        # Should be able to write something to the library now
        store = Arctic(mongo_host)
        assert store['user.library']._arctic_lib.get_library_metadata('QUOTA') == 10240 * 1024 * 1024
>       store['user.library'].write('key', {'a': 'b'})
tests/integration/scripts/test_initialize_library.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'a': 'b'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________________ test_init_library_no_arctic_prefix ______________________
mongo_host = '127.12.101.44:30878'
    def test_init_library_no_arctic_prefix(mongo_host):
        # Create the user agains the current mongo database
        with patch('arctic.scripts.arctic_init_library.do_db_auth', return_value=True), \
             patch('pymongo.database.Database.authenticate', return_value=True):
            run_as_main(mil.main, '--host', mongo_host, '--library', 'user.library')
    
        # Should be able to write something to the library now
        store = Arctic(mongo_host)
        assert store['user.library']._arctic_lib.get_library_metadata('QUOTA') == 10240 * 1024 * 1024
>       store['user.library'].write('key', {'a': 'b'})
tests/integration/scripts/test_initialize_library.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'a': 'b'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________________________ test_prune_versions_full ___________________________
mongo_host = '127.12.101.44:8226'
library = <VersionStore at 0x7fa61e595438>
    <ArcticLibrary at 0x7fa61d894eb8, arctic_test.TEST>
        <Arctic at 0x7fa61e73ef98, connected to MongoClient(host=['127.12.101.44:8226'], document_class=dict, tz_aware=False, connect=True)>
library_name = 'test.TEST'
    def test_prune_versions_full(mongo_host, library, library_name):
        with patch('arctic.scripts.arctic_prune_versions.do_db_auth', return_value=True):
            # Write some stuff with snapshots
            library.snapshot('snap')
>           library.write('symbol', "val1")
tests/integration/scripts/test_prune_versions.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'val1'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_keep_recent_snapshots __________________________
library = <VersionStore at 0x7fa61e5b52e8>
    <ArcticLibrary at 0x7fa61e5b58d0, arctic_test.TEST>
        <Arctic at 0x7fa61e5b5160, connected to MongoClient(host=['127.12.101.44:20236'], document_class=dict, tz_aware=False, connect=True)>
    def test_keep_recent_snapshots(library):
>       library.write("cherry", "blob")
tests/integration/scripts/test_prune_versions.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'blob'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________________ test_fix_broken_snapshot_references ______________________
library = <VersionStore at 0x7fa61e4d48d0>
    <ArcticLibrary at 0x7fa61e4d44a8, arctic_test.TEST>
        <Arctic at 0x7fa61e5a5be0, connected to MongoClient(host=['127.12.101.44:12121'], document_class=dict, tz_aware=False, connect=True)>
    def test_fix_broken_snapshot_references(library):
>       library.write("cherry", "blob")
tests/integration/scripts/test_prune_versions.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'blob'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_keep_only_one_version __________________________
library = <VersionStore at 0x7fa61e40d2b0>
    <ArcticLibrary at 0x7fa61e40db70, arctic_test.TEST>
        <Arctic at 0x7fa61e7f45c0, connected to MongoClient(host=['127.12.101.44:25453'], document_class=dict, tz_aware=False, connect=True)>
    def test_keep_only_one_version(library):
>       library.write("cherry", "blob")
tests/integration/scripts/test_prune_versions.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'blob'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_write_ts_with_column_name_same_as_observed_dt_ok _____________
bitemporal_library = <arctic.store.bitemporal_store.BitemporalStore object at 0x7fa61e5b7f28>
    def test_write_ts_with_column_name_same_as_observed_dt_ok(bitemporal_library):
        ts1 = read_str_as_pandas("""       sample_dt | observed_dt | near
                             2012-09-08 17:06:11.040 |    2015-1-1 |  1.0
                             2012-10-08 17:06:11.040 |    2015-1-1 |  2.0
                             2012-10-09 17:06:11.040 |    2015-1-1 |  2.5
                             2012-11-08 17:06:11.040 |    2015-1-1 |  3.0""")
>       bitemporal_library.update('spam', ts1)
tests/integration/store/test_bitemporal_store.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/store/bitemporal_store.py:94: in update
    self._store.write(symbol, df, metadata=metadata, prune_previous_version=True)
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data =                                                             observed_dt  near
sample_dt               observed_dt     ...4:18:44.559585+00:00      2015-1-1    2.5
2012-11-08 17:06:11.040 2021-01-20 04:18:44.559585+00:00      2015-1-1    3.0
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________ test_write_new_column_name_to_arctic_1_40_data ________________
ndarray_store_with_uncompressed_write = {'store': <VersionStore at 0x7fa61e5caba8>
    <ArcticLibrary at 0x7fa61e5ca940, arctic_test.TEST>
        <Arctic at ...ed to MongoClient(host=['127.12.101.44:26959'], document_class=dict, tz_aware=False, connect=True)>, 'symbol': 'MYARR'}
    def test_write_new_column_name_to_arctic_1_40_data(ndarray_store_with_uncompressed_write):
        store = ndarray_store_with_uncompressed_write['store']
        symbol = ndarray_store_with_uncompressed_write['symbol']
    
        arr = store.read(symbol).data
        new_arr = np.array(list(arr) + [(2,)], dtype=[('fgh', '<i8')])
    
>       store.write(symbol, new_arr)
tests/integration/store/test_ndarray_store.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(0,), (1,), (2,)], dtype=[('fgh', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________________ test_save_read_simple_ndarray _________________________
library = <VersionStore at 0x7fa61e5cd518>
    <ArcticLibrary at 0x7fa61e4d47b8, arctic_test.TEST>
        <Arctic at 0x7fa630cc35f8, connected to MongoClient(host=['127.12.101.44:27730'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_simple_ndarray(library):
        ndarr = np.ones(1000)
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., ...1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_save_read_big_1darray[FwPointersCfg.DISABLED] ______________
library = <VersionStore at 0x7fa61e591da0>
    <ArcticLibrary at 0x7fa61e591320, arctic_test.TEST>
        <Arctic at 0x7fa61e79e208, connected to MongoClient(host=['127.12.101.44:4661'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_read_big_1darray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.random.rand(5326, 6020).ravel()
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([0.628746  , 0.53697555, 0.79621416, ..., 0.91982578, 0.0803268 ,
       0.98696542])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_save_read_big_1darray[FwPointersCfg.HYBRID] _______________
library = <VersionStore at 0x7fa61e5f6e48>
    <ArcticLibrary at 0x7fa61e5f6240, arctic_test.TEST>
        <Arctic at 0x7fa61e515ef0, connected to MongoClient(host=['127.12.101.44:32573'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_read_big_1darray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.random.rand(5326, 6020).ravel()
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([0.63711833, 0.06096944, 0.42971039, ..., 0.98057167, 0.53728828,
       0.23179966])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_save_read_big_1darray[FwPointersCfg.ENABLED] _______________
library = <VersionStore at 0x7fa61e5825f8>
    <ArcticLibrary at 0x7fa630ca9470, arctic_test.TEST>
        <Arctic at 0x7fa61e5cd2e8, connected to MongoClient(host=['127.12.101.44:27784'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_read_big_1darray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.random.rand(5326, 6020).ravel()
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([0.06281407, 0.39837828, 0.4818402 , ..., 0.52608253, 0.03126608,
       0.9509533 ])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_save_and_resave_reuses_chunks[FwPointersCfg.DISABLED] __________
library = <VersionStore at 0x7fa61e78d9e8>
    <ArcticLibrary at 0x7fa61e57dd30, arctic_test.TEST>
        <Arctic at 0x7fa630d557b8, connected to MongoClient(host=['127.12.101.44:31862'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_and_resave_reuses_chunks(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            with patch('arctic.store._ndarray_store._CHUNK_SIZE', 1000):
                ndarr = np.random.rand(1024)
>               library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([0.38241349, 0.974596  , 0.19934355, ..., 0.21694305, 0.05187301,
       0.26789656])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_save_and_resave_reuses_chunks[FwPointersCfg.HYBRID] ___________
library = <VersionStore at 0x7fa61e3c07f0>
    <ArcticLibrary at 0x7fa61e3c0ac8, arctic_test.TEST>
        <Arctic at 0x7fa61e3c06d8, connected to MongoClient(host=['127.12.101.44:10695'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_and_resave_reuses_chunks(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            with patch('arctic.store._ndarray_store._CHUNK_SIZE', 1000):
                ndarr = np.random.rand(1024)
>               library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([0.57478177, 0.48572512, 0.66992454, ..., 0.8726358 , 0.55752944,
       0.60225151])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_save_and_resave_reuses_chunks[FwPointersCfg.ENABLED] ___________
library = <VersionStore at 0x7fa61e4d0898>
    <ArcticLibrary at 0x7fa61e4d0940, arctic_test.TEST>
        <Arctic at 0x7fa61e4d0278, connected to MongoClient(host=['127.12.101.44:20140'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_and_resave_reuses_chunks(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            with patch('arctic.store._ndarray_store._CHUNK_SIZE', 1000):
                ndarr = np.random.rand(1024)
>               library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([0.31901613, 0.57107943, 0.05769164, ..., 0.22299145, 0.52197263,
       0.74784986])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_save_read_big_2darray[FwPointersCfg.DISABLED] ______________
library = <VersionStore at 0x7fa61e538f98>
    <ArcticLibrary at 0x7fa61e6c3198, arctic_test.TEST>
        <Arctic at 0x7fa61e538d30, connected to MongoClient(host=['127.12.101.44:20822'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_read_big_2darray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.random.rand(5326, 6020)
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:93: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([[0.74866432, 0.96520491, 0.74788645, ..., 0.53932683, 0.99916432,
        0.91244513],
       [0.85408431, 0.43...99,
        0.83693053],
       [0.82470477, 0.78415333, 0.26017648, ..., 0.95383268, 0.58433853,
        0.52885696]])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_save_read_big_2darray[FwPointersCfg.HYBRID] _______________
library = <VersionStore at 0x7fa61e4d3da0>
    <ArcticLibrary at 0x7fa61e4d32b0, arctic_test.TEST>
        <Arctic at 0x7fa61e5cc9e8, connected to MongoClient(host=['127.12.101.44:14662'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_read_big_2darray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.random.rand(5326, 6020)
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:93: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([[0.28511925, 0.85967508, 0.19147288, ..., 0.42551193, 0.02061601,
        0.18248676],
       [0.42852919, 0.57...23,
        0.33468928],
       [0.67081149, 0.27724778, 0.05745847, ..., 0.66727037, 0.79350586,
        0.68531092]])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_save_read_big_2darray[FwPointersCfg.ENABLED] _______________
library = <VersionStore at 0x7fa61e73e5c0>
    <ArcticLibrary at 0x7fa61e73e240, arctic_test.TEST>
        <Arctic at 0x7fa61e73e3c8, connected to MongoClient(host=['127.12.101.44:13263'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_read_big_2darray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.random.rand(5326, 6020)
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:93: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([[0.53683868, 0.90322104, 0.35427793, ..., 0.4325776 , 0.87999134,
        0.7733913 ],
       [0.89116675, 0.37...17,
        0.25209646],
       [0.45121587, 0.01783864, 0.47912721, ..., 0.96016921, 0.9628424 ,
        0.69375493]])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_get_info_bson_object ___________________________
library = <VersionStore at 0x7fa61e3a50b8>
    <ArcticLibrary at 0x7fa61e3a5080, arctic_test.TEST>
        <Arctic at 0x7fa61e58ec18, connected to MongoClient(host=['127.12.101.44:12409'], document_class=dict, tz_aware=False, connect=True)>
    def test_get_info_bson_object(library):
        ndarr = np.ones(1000)
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:100: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., ...1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________________ test_save_read_ndarray_with_array_field ____________________
library = <VersionStore at 0x7fa61e371ac8>
    <ArcticLibrary at 0x7fa61e371c18, arctic_test.TEST>
        <Arctic at 0x7fa61e519748, connected to MongoClient(host=['127.12.101.44:6296'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_ndarray_with_array_field(library):
        ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
        ndarr['A'] = 1
        ndarr['B'] = 2
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:108: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.])],
      dtype=[('A', '<i8'), ('B', '<f8', (2,))])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________________________ test_save_read_ndarray ____________________________
library = <VersionStore at 0x7fa61e3628d0>
    <ArcticLibrary at 0x7fa61e712358, arctic_test.TEST>
        <Arctic at 0x7fa61e3627b8, connected to MongoClient(host=['127.12.101.44:17123'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_ndarray(library):
        ndarr = np.empty(1000, dtype=[('abc', 'int64')])
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:115: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(    140352304452168,), (    140352304452168,),
       (           84892544,), (           84892544,),
       (...327916,), (8316308347820453733,),
       (7809652371833321007,), (7526774399982530149,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________________ test_multiple_write[FwPointersCfg.DISABLED] __________________
library = <VersionStore at 0x7fa61e33d128>
    <ArcticLibrary at 0x7fa61e5bdd30, arctic_test.TEST>
        <Arctic at 0x7fa61e33dac8, connected to MongoClient(host=['127.12.101.44:19405'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_multiple_write(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.empty(1000, dtype=[('abc', 'int64')])
            foo = np.empty(900, dtype=[('abc', 'int64')])
>           library.write('MYARR', foo)
tests/integration/store/test_ndarray_store.py:125: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(    140352304452344,), (    140352304452344,),
       (           84989808,), (           84989808,),
       (...005809,), (2308706314327636017,),
       (4046519587542409248,), (4121696569436354100,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________ test_multiple_write[FwPointersCfg.HYBRID] ___________________
library = <VersionStore at 0x7fa61e722668>
    <ArcticLibrary at 0x7fa61e7220b8, arctic_test.TEST>
        <Arctic at 0x7fa61e4c9da0, connected to MongoClient(host=['127.12.101.44:18801'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_multiple_write(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.empty(1000, dtype=[('abc', 'int64')])
            foo = np.empty(900, dtype=[('abc', 'int64')])
>           library.write('MYARR', foo)
tests/integration/store/test_ndarray_store.py:125: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(    140352304452120,), (    140352304452120,),
       (           84805552,), (           84805552,),
       (...091059,), (3690756206755394608,),
       (4121134727618442288,), (2314861393254036021,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________ test_multiple_write[FwPointersCfg.ENABLED] __________________
library = <VersionStore at 0x7fa61e514a90>
    <ArcticLibrary at 0x7fa61e514128, arctic_test.TEST>
        <Arctic at 0x7fa61e722898, connected to MongoClient(host=['127.12.101.44:23022'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_multiple_write(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.empty(1000, dtype=[('abc', 'int64')])
            foo = np.empty(900, dtype=[('abc', 'int64')])
>           library.write('MYARR', foo)
tests/integration/store/test_ndarray_store.py:125: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(    140352304452168,), (           83618496,),
       (           83618496,), (           83618496,),
       (...163385,), (3616729378852321329,),
       (3761975942985496118,), (2314861393254036535,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________________________ test_save_read_large_ndarray _________________________
library = <VersionStore at 0x7fa61e521320>
    <ArcticLibrary at 0x7fa61e521160, arctic_test.TEST>
        <Arctic at 0x7fa61e7ed9e8, connected to MongoClient(host=['127.12.101.44:18493'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_large_ndarray(library):
        dtype = np.dtype([('abc', 'int64')])
        ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
        assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:147: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4705698654206296064,),
       (4705698656353779712,), (4705698658501263360,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________________________ test_mutable_ndarray _____________________________
library = <VersionStore at 0x7fa61e363ac8>
    <ArcticLibrary at 0x7fa61e363eb8, arctic_test.TEST>
        <Arctic at 0x7fa61e363d68, connected to MongoClient(host=['127.12.101.44:21502'], document_class=dict, tz_aware=False, connect=True)>
    def test_mutable_ndarray(library):
        dtype = np.dtype([('abc', 'int64')])
        ndarr = np.arange(32).view(dtype=dtype)
        ndarr.setflags(write=True)
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store.py:156: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([( 0,), ( 1,), ( 2,), ( 3,), ( 4,), ( 5,), ( 6,), ( 7,), ( 8,),
       ( 9,), (10,), (11,), (12,), (13,), (14,),...,), (20,), (21,), (22,), (23,), (24,), (25,), (26,),
       (27,), (28,), (29,), (30,), (31,)], dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_append_simple_ndarray[FwPointersCfg.DISABLED] ______________
library = <VersionStore at 0x7fa61e5c09e8>
    <ArcticLibrary at 0x7fa61e5c0748, arctic_test.TEST>
        <Arctic at 0x7fa61e5d39b0, connected to MongoClient(host=['127.12.101.44:1729'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_simple_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.ones(1000, dtype='int64')
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_append_simple_ndarray[FwPointersCfg.HYBRID] _______________
library = <VersionStore at 0x7fa61e4c9eb8>
    <ArcticLibrary at 0x7fa61e4c93c8, arctic_test.TEST>
        <Arctic at 0x7fa61e6997f0, connected to MongoClient(host=['127.12.101.44:23117'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_simple_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.ones(1000, dtype='int64')
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_append_simple_ndarray[FwPointersCfg.ENABLED] _______________
library = <VersionStore at 0x7fa61e65c748>
    <ArcticLibrary at 0x7fa61e65ca20, arctic_test.TEST>
        <Arctic at 0x7fa61e65cc18, connected to MongoClient(host=['127.12.101.44:30307'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_simple_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.ones(1000, dtype='int64')
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_append_simple_ndarray_promoting_types[FwPointersCfg.DISABLED] ______
library = <VersionStore at 0x7fa61e40d898>
    <ArcticLibrary at 0x7fa61e40d128, arctic_test.TEST>
        <Arctic at 0x7fa61e40d278, connected to MongoClient(host=['127.12.101.44:22023'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_simple_ndarray_promoting_types(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.ones(100, dtype='int64')
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_append_simple_ndarray_promoting_types[FwPointersCfg.HYBRID] _______
library = <VersionStore at 0x7fa61e65c2e8>
    <ArcticLibrary at 0x7fa61e65cd68, arctic_test.TEST>
        <Arctic at 0x7fa61e79eda0, connected to MongoClient(host=['127.12.101.44:11965'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_simple_ndarray_promoting_types(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.ones(100, dtype='int64')
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_append_simple_ndarray_promoting_types[FwPointersCfg.ENABLED] _______
library = <VersionStore at 0x7fa61e4d0e48>
    <ArcticLibrary at 0x7fa61e4d0d30, arctic_test.TEST>
        <Arctic at 0x7fa61e67aef0, connected to MongoClient(host=['127.12.101.44:13192'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_simple_ndarray_promoting_types(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.ones(100, dtype='int64')
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________________________ test_promote_types ______________________________
library = <VersionStore at 0x7fa61e3ca780>
    <ArcticLibrary at 0x7fa61e3ca048, arctic_test.TEST>
        <Arctic at 0x7fa61e67a710, connected to MongoClient(host=['127.12.101.44:25045'], document_class=dict, tz_aware=False, connect=True)>
    def test_promote_types(library):
        ndarr = np.empty(1000, dtype=[('abc', 'int64')])
>       library.write('MYARR', ndarr[:800])
tests/integration/store/test_ndarray_store_append.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(140352304452104,), (      116587584,), (              0,),
       (              0,), (140351448640240,), (140...4032,), (140351448905528,), (140351449938944,),
       (140351449988192,), (140351449128560,)], dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________________________ test_promote_types2 ______________________________
library = <VersionStore at 0x7fa61e3da208>
    <ArcticLibrary at 0x7fa61e3dac50, arctic_test.TEST>
        <Arctic at 0x7fa61e5d3f60, connected to MongoClient(host=['127.12.101.44:19353'], document_class=dict, tz_aware=False, connect=True)>
    def test_promote_types2(library):
        ndarr = np.array(np.arange(1000), dtype=[('abc', 'float64')])
>       library.write('MYARR', ndarr[:800])
tests/integration/store/test_ndarray_store_append.py:48: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(  0.,), (  1.,), (  2.,), (  3.,), (  4.,), (  5.,), (  6.,),
       (  7.,), (  8.,), (  9.,), ( 10.,), ( 11....       (791.,), (792.,), (793.,), (794.,), (795.,), (796.,), (797.,),
       (798.,), (799.,)], dtype=[('abc', '<f8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________________ test_promote_types_smaller_sizes _______________________
library = <VersionStore at 0x7fa61e4224a8>
    <ArcticLibrary at 0x7fa61e422780, arctic_test.TEST>
        <Arctic at 0x7fa61e749630, connected to MongoClient(host=['127.12.101.44:7120'], document_class=dict, tz_aware=False, connect=True)>
    def test_promote_types_smaller_sizes(library):
>       library.write('MYARR', np.ones(100, dtype='int64'))
tests/integration/store/test_ndarray_store_append.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________________ test_promote_types_larger_sizes ________________________
library = <VersionStore at 0x7fa61e389390>
    <ArcticLibrary at 0x7fa61e389fd0, arctic_test.TEST>
        <Arctic at 0x7fa61e389358, connected to MongoClient(host=['127.12.101.44:11773'], document_class=dict, tz_aware=False, connect=True)>
    def test_promote_types_larger_sizes(library):
>       library.write('MYARR', np.ones(100, dtype='int32'))
tests/integration/store/test_ndarray_store_append.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int32)
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________________ test_promote_field_types_smaller_sizes ____________________
library = <VersionStore at 0x7fa61e4fdf98>
    <ArcticLibrary at 0x7fa61e4fdb00, arctic_test.TEST>
        <Arctic at 0x7fa61e4fd550, connected to MongoClient(host=['127.12.101.44:20603'], document_class=dict, tz_aware=False, connect=True)>
    def test_promote_field_types_smaller_sizes(library):
        arr = np.array([(3, 7)], dtype=[('a', '<i8'), ('b', '<i8')])
>       library.write('MYARR', arr)
tests/integration/store/test_ndarray_store_append.py:70: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(3, 7)], dtype=[('a', '<i8'), ('b', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________________ test_promote_field_types_larger_sizes _____________________
library = <VersionStore at 0x7fa61e3ba710>
    <ArcticLibrary at 0x7fa61e3bab00, arctic_test.TEST>
        <Arctic at 0x7fa61e6ce8d0, connected to MongoClient(host=['127.12.101.44:16203'], document_class=dict, tz_aware=False, connect=True)>
    def test_promote_field_types_larger_sizes(library):
        arr = np.array([(3, 7)], dtype=[('a', '<i4'), ('b', '<i8')])
>       library.write('MYARR', arr)
tests/integration/store/test_ndarray_store_append.py:80: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(3, 7)], dtype=[('a', '<i4'), ('b', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________ test_append_ndarray_with_field_shape[FwPointersCfg.DISABLED] _________
library = <VersionStore at 0x7fa61e699e48>
    <ArcticLibrary at 0x7fa61e699780, arctic_test.TEST>
        <Arctic at 0x7fa61e699c88, connected to MongoClient(host=['127.12.101.44:4302'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_ndarray_with_field_shape(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
            ndarr['A'] = 1
            ndarr['B'] = 2
            ndarr2 = np.empty(10, dtype=[('A', 'int64'), ('B', 'int64', (2,))])
            ndarr2['A'] = 1
            ndarr2['B'] = 2
    
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:98: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.])],
      dtype=[('A', '<i8'), ('B', '<f8', (2,))])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_append_ndarray_with_field_shape[FwPointersCfg.HYBRID] __________
library = <VersionStore at 0x7fa61e43bb00>
    <ArcticLibrary at 0x7fa61e43b6d8, arctic_test.TEST>
        <Arctic at 0x7fa61e3f5128, connected to MongoClient(host=['127.12.101.44:14858'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_ndarray_with_field_shape(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
            ndarr['A'] = 1
            ndarr['B'] = 2
            ndarr2 = np.empty(10, dtype=[('A', 'int64'), ('B', 'int64', (2,))])
            ndarr2['A'] = 1
            ndarr2['B'] = 2
    
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:98: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.])],
      dtype=[('A', '<i8'), ('B', '<f8', (2,))])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________ test_append_ndarray_with_field_shape[FwPointersCfg.ENABLED] __________
library = <VersionStore at 0x7fa61e52b668>
    <ArcticLibrary at 0x7fa61e52bb38, arctic_test.TEST>
        <Arctic at 0x7fa61e52bef0, connected to MongoClient(host=['127.12.101.44:25312'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_ndarray_with_field_shape(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
            ndarr['A'] = 1
            ndarr['B'] = 2
            ndarr2 = np.empty(10, dtype=[('A', 'int64'), ('B', 'int64', (2,))])
            ndarr2['A'] = 1
            ndarr2['B'] = 2
    
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:98: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]), (1, [2., 2.]),
       (1, [2., 2.]), (1, [2., 2.])],
      dtype=[('A', '<i8'), ('B', '<f8', (2,))])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_append_read_large_ndarray[FwPointersCfg.DISABLED] ____________
library = <VersionStore at 0x7fa61e66cc18>
    <ArcticLibrary at 0x7fa61e66c710, arctic_test.TEST>
        <Arctic at 0x7fa61e7d7a58, connected to MongoClient(host=['127.12.101.44:1703'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_read_large_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(50 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
            assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>           library.write('MYARR1', ndarr)
tests/integration/store/test_ndarray_store_append.py:113: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4708794882171338752,),
       (4708794883245080576,), (4708794884318822400,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_append_read_large_ndarray[FwPointersCfg.HYBRID] _____________
library = <VersionStore at 0x7fa61e4c9860>
    <ArcticLibrary at 0x7fa61e4c94e0, arctic_test.TEST>
        <Arctic at 0x7fa61e57d0f0, connected to MongoClient(host=['127.12.101.44:9351'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_read_large_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(50 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
            assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>           library.write('MYARR1', ndarr)
tests/integration/store/test_ndarray_store_append.py:113: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4708794882171338752,),
       (4708794883245080576,), (4708794884318822400,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_append_read_large_ndarray[FwPointersCfg.ENABLED] _____________
library = <VersionStore at 0x7fa61e7ce0b8>
    <ArcticLibrary at 0x7fa61e7ce630, arctic_test.TEST>
        <Arctic at 0x7fa61e776320, connected to MongoClient(host=['127.12.101.44:22126'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_read_large_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(50 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
            assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>           library.write('MYARR1', ndarr)
tests/integration/store/test_ndarray_store_append.py:113: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4708794882171338752,),
       (4708794883245080576,), (4708794884318822400,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_save_append_read_ndarray[FwPointersCfg.DISABLED] _____________
library = <VersionStore at 0x7fa61e4f1278>
    <ArcticLibrary at 0x7fa61e4f1a90, arctic_test.TEST>
        <Arctic at 0x7fa61e4f10b8, connected to MongoClient(host=['127.12.101.44:9211'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_append_read_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
            assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4705698654206296064,),
       (4705698656353779712,), (4705698658501263360,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_save_append_read_ndarray[FwPointersCfg.HYBRID] ______________
library = <VersionStore at 0x7fa61e402f28>
    <ArcticLibrary at 0x7fa61e402240, arctic_test.TEST>
        <Arctic at 0x7fa61e367400, connected to MongoClient(host=['127.12.101.44:9440'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_append_read_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
            assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4705698654206296064,),
       (4705698656353779712,), (4705698658501263360,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_save_append_read_ndarray[FwPointersCfg.ENABLED] _____________
library = <VersionStore at 0x7fa61e52d0b8>
    <ArcticLibrary at 0x7fa61e52d6a0, arctic_test.TEST>
        <Arctic at 0x7fa61e691f28, connected to MongoClient(host=['127.12.101.44:30860'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_append_read_ndarray(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
            assert len(ndarr.tobytes()) > 16 * 1024 * 1024                      # FIXME: CM#007 - (deprecated tostring)
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4705698654206296064,),
       (4705698656353779712,), (4705698658501263360,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________________ test_save_append_read_1row_ndarray ______________________
library = <VersionStore at 0x7fa61e5e4d30>
    <ArcticLibrary at 0x7fa61e5e4e10, arctic_test.TEST>
        <Arctic at 0x7fa61e684cf8, connected to MongoClient(host=['127.12.101.44:8181'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_append_read_1row_ndarray(library):
        dtype = np.dtype([('abc', 'int64')])
        ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
        assert len(ndarr.tobytes()) > 16 * 1024 * 1024                          # FIXME: CM#007 - (deprecated tostring)
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:156: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4705698654206296064,),
       (4705698656353779712,), (4705698658501263360,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________________ test_append_too_large_ndarray _________________________
library = <VersionStore at 0x7fa61e3e3ba8>
    <ArcticLibrary at 0x7fa61e3e3fd0, arctic_test.TEST>
        <Arctic at 0x7fa61e52d4a8, connected to MongoClient(host=['127.12.101.44:10103'], document_class=dict, tz_aware=False, connect=True)>
    def test_append_too_large_ndarray(library):
        dtype = np.dtype([('abc', 'int64')])
        ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
        assert len(ndarr.tobytes()) > 16 * 1024 * 1024                          # FIXME: CM#007 - (deprecated tostring)
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:173: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), ..., (4705698654206296064,),
       (4705698656353779712,), (4705698658501263360,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________ test_empty_field_append_keeps_all_columns ___________________
library = <VersionStore at 0x7fa61e43b978>
    <ArcticLibrary at 0x7fa61e5bd978, arctic_test.TEST>
        <Arctic at 0x7fa61e5bda58, connected to MongoClient(host=['127.12.101.44:20834'], document_class=dict, tz_aware=False, connect=True)>
    def test_empty_field_append_keeps_all_columns(library):
        ndarr = np.array([(3, 5)], dtype=[('a', '<i'), ('b', '<i')])
        ndarr2 = np.array([], dtype=[('a', '<i')])
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:182: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(3, 5)], dtype=[('a', '<i4'), ('b', '<i4')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_empty_append_promotes_dtype[FwPointersCfg.DISABLED] ___________
library = <VersionStore at 0x7fa61e7dba90>
    <ArcticLibrary at 0x7fa61e7db8d0, arctic_test.TEST>
        <Arctic at 0x7fa61e728588, connected to MongoClient(host=['127.12.101.44:1967'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_promotes_dtype(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array(["a", "b", "c"])
            ndarr2 = np.array([])
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:193: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_empty_append_promotes_dtype[FwPointersCfg.HYBRID] ____________
library = <VersionStore at 0x7fa61e5913c8>
    <ArcticLibrary at 0x7fa61e591be0, arctic_test.TEST>
        <Arctic at 0x7fa61e64d1d0, connected to MongoClient(host=['127.12.101.44:32308'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_promotes_dtype(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array(["a", "b", "c"])
            ndarr2 = np.array([])
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:193: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_empty_append_promotes_dtype[FwPointersCfg.ENABLED] ____________
library = <VersionStore at 0x7fa61e66f9b0>
    <ArcticLibrary at 0x7fa61e66f3c8, arctic_test.TEST>
        <Arctic at 0x7fa61e64d400, connected to MongoClient(host=['127.12.101.44:25584'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_promotes_dtype(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array(["a", "b", "c"])
            ndarr2 = np.array([])
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:193: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________________ test_empty_append_promotes_dtype2 _______________________
library = <VersionStore at 0x7fa61e699668>
    <ArcticLibrary at 0x7fa61e6998d0, arctic_test.TEST>
        <Arctic at 0x7fa61e290c50, connected to MongoClient(host=['127.12.101.44:27469'], document_class=dict, tz_aware=False, connect=True)>
    def test_empty_append_promotes_dtype2(library):
        ndarr = np.array([])
        ndarr2 = np.array(["a", "b", "c"])
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:202: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([], dtype=float64)
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________________ test_empty_append_promotes_dtype3 _______________________
library = <VersionStore at 0x7fa61e7307b8>
    <ArcticLibrary at 0x7fa61e730ba8, arctic_test.TEST>
        <Arctic at 0x7fa61e7d4b70, connected to MongoClient(host=['127.12.101.44:3531'], document_class=dict, tz_aware=False, connect=True)>
    def test_empty_append_promotes_dtype3(library):
        ndarr = np.array([])
        ndarr2 = np.array(["a", "b", "c"])
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:211: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([], dtype=float64)
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________________ test_convert_to_structured_array _______________________
library = <VersionStore at 0x7fa61e4a0ac8>
    <ArcticLibrary at 0x7fa61e4a0a58, arctic_test.TEST>
        <Arctic at 0x7fa61e2a9240, connected to MongoClient(host=['127.12.101.44:29697'], document_class=dict, tz_aware=False, connect=True)>
    def test_convert_to_structured_array(library):
        arr = np.ones(100, dtype='int64')
>       library.write('MYARR', arr)
tests/integration/store/test_ndarray_store_append.py:221: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________ test_empty_append_concat_and_rewrite[FwPointersCfg.DISABLED] _________
library = <VersionStore at 0x7fa61e7b4ef0>
    <ArcticLibrary at 0x7fa61e7b4fd0, arctic_test.TEST>
        <Arctic at 0x7fa61e7b4ac8, connected to MongoClient(host=['127.12.101.44:17554'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array([])
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:232: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([], dtype=float64)
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_empty_append_concat_and_rewrite[FwPointersCfg.HYBRID] __________
library = <VersionStore at 0x7fa61e2a0630>
    <ArcticLibrary at 0x7fa61e2a05f8, arctic_test.TEST>
        <Arctic at 0x7fa61e2a0128, connected to MongoClient(host=['127.12.101.44:4096'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array([])
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:232: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([], dtype=float64)
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________ test_empty_append_concat_and_rewrite[FwPointersCfg.ENABLED] __________
library = <VersionStore at 0x7fa61e3e3080>
    <ArcticLibrary at 0x7fa61e3e3ef0, arctic_test.TEST>
        <Arctic at 0x7fa61e79eef0, connected to MongoClient(host=['127.12.101.44:29622'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array([])
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:232: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([], dtype=float64)
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_empty_append_concat_and_rewrite_2[FwPointersCfg.DISABLED] ________
library = <VersionStore at 0x7fa61e6a07f0>
    <ArcticLibrary at 0x7fa61e6a0f98, arctic_test.TEST>
        <Arctic at 0x7fa61e76b7f0, connected to MongoClient(host=['127.12.101.44:21207'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite_2(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr2)
tests/integration/store/test_ndarray_store_append.py:244: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________ test_empty_append_concat_and_rewrite_2[FwPointersCfg.HYBRID] _________
library = <VersionStore at 0x7fa61e4d4a20>
    <ArcticLibrary at 0x7fa61e4d4208, arctic_test.TEST>
        <Arctic at 0x7fa61e75c2b0, connected to MongoClient(host=['127.12.101.44:26637'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite_2(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr2)
tests/integration/store/test_ndarray_store_append.py:244: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_empty_append_concat_and_rewrite_2[FwPointersCfg.ENABLED] _________
library = <VersionStore at 0x7fa61e3625f8>
    <ArcticLibrary at 0x7fa61e362860, arctic_test.TEST>
        <Arctic at 0x7fa61e75c5f8, connected to MongoClient(host=['127.12.101.44:14866'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite_2(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr2)
tests/integration/store/test_ndarray_store_append.py:244: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_empty_append_concat_and_rewrite_3[FwPointersCfg.DISABLED] ________
library = <VersionStore at 0x7fa61e38b898>
    <ArcticLibrary at 0x7fa61e38b2b0, arctic_test.TEST>
        <Arctic at 0x7fa61e3bacc0, connected to MongoClient(host=['127.12.101.44:11439'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite_3(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array([])
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr2)
tests/integration/store/test_ndarray_store_append.py:256: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________ test_empty_append_concat_and_rewrite_3[FwPointersCfg.HYBRID] _________
library = <VersionStore at 0x7fa61e728dd8>
    <ArcticLibrary at 0x7fa61e6992b0, arctic_test.TEST>
        <Arctic at 0x7fa61e728198, connected to MongoClient(host=['127.12.101.44:10456'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite_3(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array([])
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr2)
tests/integration/store/test_ndarray_store_append.py:256: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_empty_append_concat_and_rewrite_3[FwPointersCfg.ENABLED] _________
library = <VersionStore at 0x7fa61e515dd8>
    <ArcticLibrary at 0x7fa61e515ba8, arctic_test.TEST>
        <Arctic at 0x7fa61e699ef0, connected to MongoClient(host=['127.12.101.44:17857'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_empty_append_concat_and_rewrite_3(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            ndarr = np.array([])
            ndarr2 = np.array(["a", "b", "c"])
>           library.write('MYARR', ndarr2)
tests/integration/store/test_ndarray_store_append.py:256: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array(['a', 'b', 'c'], dtype='<U1')
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________________ test_append_with_extra_columns ________________________
library = <VersionStore at 0x7fa61e511588>
    <ArcticLibrary at 0x7fa61e3ba4a8, arctic_test.TEST>
        <Arctic at 0x7fa61e5cd4a8, connected to MongoClient(host=['127.12.101.44:16673'], document_class=dict, tz_aware=False, connect=True)>
    def test_append_with_extra_columns(library):
        ndarr = np.array([(2.1, 1, "a")], dtype=[('C', np.float), ('B', np.int), ('A', 'S1')])
        ndarr2 = np.array([("b", 2, 3.1, 'c', 4, 5.)], dtype=[('A', 'S1'), ('B', np.int), ('C', np.float),
                                                              ('D', 'S1'), ('E', np.int), ('F', np.float)])
        expected = np.array([("a", 1, 2.1, '', 0, np.nan),
                             ("b", 2, 3.1, 'c', 4, 5.)],
                            dtype=np.dtype([('A', 'S1'), ('B', np.int), ('C', np.float),
                                            ('D', 'S1'), ('E', np.int), ('F', np.float)]))
>       library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:271: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(2.1, 1, b'a')], dtype=[('C', '<f8'), ('B', '<i8'), ('A', 'S1')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_save_append_delete_append[FwPointersCfg.DISABLED] ____________
library = <VersionStore at 0x7fa61e4222b0>
    <ArcticLibrary at 0x7fa61e422b38, arctic_test.TEST>
        <Arctic at 0x7fa61e422438, connected to MongoClient(host=['127.12.101.44:21737'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_append_delete_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
>           v1 = library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:284: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), (4613937818241073152,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_save_append_delete_append[FwPointersCfg.HYBRID] _____________
library = <VersionStore at 0x7fa61e7ae908>
    <ArcticLibrary at 0x7fa61e7aeb70, arctic_test.TEST>
        <Arctic at 0x7fa61e7cf470, connected to MongoClient(host=['127.12.101.44:5085'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_append_delete_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
>           v1 = library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:284: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), (4613937818241073152,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_save_append_delete_append[FwPointersCfg.ENABLED] _____________
library = <VersionStore at 0x7fa61e4f14e0>
    <ArcticLibrary at 0x7fa61e4f1668, arctic_test.TEST>
        <Arctic at 0x7fa61e776cf8, connected to MongoClient(host=['127.12.101.44:21362'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_save_append_delete_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
>           v1 = library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:284: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), (4613937818241073152,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_append_after_failed_append[FwPointersCfg.DISABLED] ____________
library = <VersionStore at 0x7fa61e6a00f0>
    <ArcticLibrary at 0x7fa61e6a0898, arctic_test.TEST>
        <Arctic at 0x7fa61e2a93c8, connected to MongoClient(host=['127.12.101.44:24714'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_after_failed_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
    
>           v1 = library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:309: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), (4613937818241073152,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_append_after_failed_append[FwPointersCfg.HYBRID] _____________
library = <VersionStore at 0x7fa61e77d550>
    <ArcticLibrary at 0x7fa61e77db38, arctic_test.TEST>
        <Arctic at 0x7fa61e4f11d0, connected to MongoClient(host=['127.12.101.44:20156'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_after_failed_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
    
>           v1 = library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:309: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), (4613937818241073152,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_append_after_failed_append[FwPointersCfg.ENABLED] ____________
library = <VersionStore at 0x7fa61e730a58>
    <ArcticLibrary at 0x7fa61e730390, arctic_test.TEST>
        <Arctic at 0x7fa61e730a90, connected to MongoClient(host=['127.12.101.44:21534'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_after_failed_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            dtype = np.dtype([('abc', 'int64')])
            ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
    
>           v1 = library.write('MYARR', ndarr)
tests/integration/store/test_ndarray_store_append.py:309: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(                  0,), (4607182418800017408,),
       (4611686018427387904,), (4613937818241073152,)],
      dtype=[('abc', '<i8')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________________________ test_append_reorder_columns __________________________
library = <VersionStore at 0x7fa61e7308d0>
    <ArcticLibrary at 0x7fa61e7304a8, arctic_test.TEST>
        <Arctic at 0x7fa61e5d31d0, connected to MongoClient(host=['127.12.101.44:14294'], document_class=dict, tz_aware=False, connect=True)>
    def test_append_reorder_columns(library):
        foo = np.array([(1, 2)], dtype=np.dtype([('a', 'u1'), ('b', 'u1')]))
>       library.write('MYARR', foo)
tests/integration/store/test_ndarray_store_append.py:326: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = array([(1, 2)], dtype=[('a', 'u1'), ('b', 'u1')])
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________________ test_can_write_pandas_df_with_object_columns _________________
library = <VersionStore at 0x7fa61e3daa20>
    <ArcticLibrary at 0x7fa61e3da7f0, arctic_test.TEST>
        <Arctic at 0x7fa61e5a0d30, connected to MongoClient(host=['127.12.101.44:25154'], document_class=dict, tz_aware=False, connect=True)>
    def test_can_write_pandas_df_with_object_columns(library):
        expected = DataFrame(data=dict(A=['a', 'b', None, 'c'], B=[1., 2., 3., 4.]), index=range(4))
>       library.write('objects', expected)
tests/integration/store/test_pandas_store.py:645: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data =       A    B
0     a  1.0
1     b  2.0
2  None  3.0
3     c  4.0
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________________________ test_duplicate_labels _____________________________
library = <VersionStore at 0x7fa61e389668>
    <ArcticLibrary at 0x7fa61e389a20, arctic_test.TEST>
        <Arctic at 0x7fa61e3c3048, connected to MongoClient(host=['127.12.101.44:26613'], document_class=dict, tz_aware=False, connect=True)>
    def test_duplicate_labels(library):
        ts1 = DataFrame(index=[dt(2012, 1, 1) + dtd(hours=x) for x in range(5)],
                        data=[[np.arange(5), np.arange(5, 10)]],
                        columns=['a', 'a']
                        )
>       library.write('TEST_1', ts1)
tests/integration/store/test_pandas_store.py:723: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data =                                    a                a
2012-01-01 00:00:00  [0, 1, 2, 3, 4]  [5, 6, 7, 8, 9]
2012-01-01...6, 7, 8, 9]
2012-01-01 03:00:00  [0, 1, 2, 3, 4]  [5, 6, 7, 8, 9]
2012-01-01 04:00:00  [0, 1, 2, 3, 4]  [5, 6, 7, 8, 9]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________________________ test_no_labels ________________________________
library = <VersionStore at 0x7fa61e108be0>
    <ArcticLibrary at 0x7fa61e362ac8, arctic_test.TEST>
        <Arctic at 0x7fa61e0be198, connected to MongoClient(host=['127.12.101.44:16928'], document_class=dict, tz_aware=False, connect=True)>
    def test_no_labels(library):
        ts1 = DataFrame(index=[dt(2012, 1, 1) + dtd(hours=x) for x in range(5)],
                        data=[[np.arange(5), np.arange(5, 10)]])
>       library.write('TEST_1', ts1)
tests/integration/store/test_pandas_store.py:731: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data =                                    0                1
2012-01-01 00:00:00  [0, 1, 2, 3, 4]  [5, 6, 7, 8, 9]
2012-01-01...6, 7, 8, 9]
2012-01-01 03:00:00  [0, 1, 2, 3, 4]  [5, 6, 7, 8, 9]
2012-01-01 04:00:00  [0, 1, 2, 3, 4]  [5, 6, 7, 8, 9]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________________________ test_save_read_bson ______________________________
library = <VersionStore at 0x7fa630812080>
    <ArcticLibrary at 0x7fa61e7b04e0, arctic_test.TEST>
        <Arctic at 0x7fa61e0e6a20, connected to MongoClient(host=['127.12.101.44:12020'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_bson(library):
        blob = {'foo': dt(2015, 1, 1), 'bar': ['a', 'b', ['x', 'y', 'z']]}
>       library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'bar': ['a', 'b', ['x', 'y', 'z']], 'foo': datetime.datetime(2015, 1, 1, 0, 0)}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_________________________ test_save_read_big_encodable _________________________
library = <VersionStore at 0x7fa61e4fe860>
    <ArcticLibrary at 0x7fa61e4fe588, arctic_test.TEST>
        <Arctic at 0x7fa61e78b828, connected to MongoClient(host=['127.12.101.44:2235'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_big_encodable(library):
        blob = {'foo': 'a' * 1024 * 1024 * 20}
>       library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_save_read_bson_object __________________________
library = <VersionStore at 0x7fa61e27ee48>
    <ArcticLibrary at 0x7fa61e27e240, arctic_test.TEST>
        <Arctic at 0x7fa61e2f57b8, connected to MongoClient(host=['127.12.101.44:3229'], document_class=dict, tz_aware=False, connect=True)>
    def test_save_read_bson_object(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
>       library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_get_info_bson_object ___________________________
library = <VersionStore at 0x7fa61e13fe10>
    <ArcticLibrary at 0x7fa61e13fef0, arctic_test.TEST>
        <Arctic at 0x7fa61e0e6f98, connected to MongoClient(host=['127.12.101.44:11629'], document_class=dict, tz_aware=False, connect=True)>
    def test_get_info_bson_object(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
>       library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:47: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________________________ test_bson_large_object ____________________________
library = <VersionStore at 0x7fa61e5213c8>
    <ArcticLibrary at 0x7fa61e38b9e8, arctic_test.TEST>
        <Arctic at 0x7fa61e5219e8, connected to MongoClient(host=['127.12.101.44:17146'], document_class=dict, tz_aware=False, connect=True)>
    def test_bson_large_object(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic,
                'large_thing': np.random.rand(int(2.1 * 1024 * 1024)).tobytes()}       # FIXME: CM#007 - (deprecated tostring)
        assert len(blob['large_thing']) > 16 * 1024 * 1024
>       library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'large_thing': b'.\xce\x9f\xc6j\xdb\xdb?\\\xfa\xb0GG\x9c\xe0?\xbcL\xff\xe...x99\xa5\x8e\xa9\x80\xec?t%\xabz\xcf\xc9\xe9?*\xd9aRr{\xe9?L\xd7(\x8bYY\xc9?', 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________________ test_bson_leak_objects_delete _________________________
library = <VersionStore at 0x7fa61e7b4860>
    <ArcticLibrary at 0x7fa61e7b4c18, arctic_test.TEST>
        <Arctic at 0x7fa61e4d0ef0, connected to MongoClient(host=['127.12.101.44:10380'], document_class=dict, tz_aware=False, connect=True)>
    def test_bson_leak_objects_delete(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
>       library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________________ test_bson_leak_objects_prune_previous _____________________
library = <VersionStore at 0x7fa61e2dc630>
    <ArcticLibrary at 0x7fa61e2dc438, arctic_test.TEST>
        <Arctic at 0x7fa61e4224e0, connected to MongoClient(host=['127.12.101.44:4928'], document_class=dict, tz_aware=False, connect=True)>
    def test_bson_leak_objects_prune_previous(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
    
        yesterday = dt.utcnow() - timedelta(days=1, seconds=1)
        _id = bson.ObjectId.from_datetime(yesterday)
        with patch("bson.ObjectId", return_value=_id):
>           library.write('BLOB', blob)
tests/integration/store/test_pickle_store.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________ test_prune_previous_doesnt_kill_other_objects _________________
library = <VersionStore at 0x7fa61e363860>
    <ArcticLibrary at 0x7fa61e3638d0, arctic_test.TEST>
        <Arctic at 0x7fa61e363b00, connected to MongoClient(host=['127.12.101.44:6970'], document_class=dict, tz_aware=False, connect=True)>
    def test_prune_previous_doesnt_kill_other_objects(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
    
        yesterday = dt.utcnow() - timedelta(days=1, seconds=1)
        _id = bson.ObjectId.from_datetime(yesterday)
        with patch("bson.ObjectId", return_value=_id):
>           library.write('BLOB', blob, prune_previous_version=False)
tests/integration/store/test_pickle_store.py:98: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________________________ test_write_metadata ______________________________
library = <VersionStore at 0x7fa61e3ecb00>
    <ArcticLibrary at 0x7fa61e3eca58, arctic_test.TEST>
        <Arctic at 0x7fa61e6c8518, connected to MongoClient(host=['127.12.101.44:3081'], document_class=dict, tz_aware=False, connect=True)>
    def test_write_metadata(library):
        blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
>       library.write(symbol='symX', data=blob, metadata={'key1': 'value1'})
tests/integration/store/test_pickle_store.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': datetime.datetime(2015, 1, 1, 0, 0), 'object': <class 'arctic.arctic.Arctic'>}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.DISABLED] ______
library = <VersionStore at 0x7fa61e297f28>
    <ArcticLibrary at 0x7fa61e297e10, arctic_test.TEST>
        <Arctic at 0x7fa61e3e3198, connected to MongoClient(host=['127.12.101.44:28966'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_read_metadata_throws_on_deleted_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1, metadata={'key': 'value'})
>           library.delete(symbol)
tests/integration/store/test_version_store.py:214: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.HYBRID] _______
library = <VersionStore at 0x7fa61c3c27f0>
    <ArcticLibrary at 0x7fa61c3c2828, arctic_test.TEST>
        <Arctic at 0x7fa61c3bca90, connected to MongoClient(host=['127.12.101.44:3322'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_read_metadata_throws_on_deleted_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1, metadata={'key': 'value'})
>           library.delete(symbol)
tests/integration/store/test_version_store.py:214: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.ENABLED] ______
library = <VersionStore at 0x7fa630cc8c50>
    <ArcticLibrary at 0x7fa61e1e4cc0, arctic_test.TEST>
        <Arctic at 0x7fa61c647ac8, connected to MongoClient(host=['127.12.101.44:20063'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_read_metadata_throws_on_deleted_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1, metadata={'key': 'value'})
>           library.delete(symbol)
tests/integration/store/test_version_store.py:214: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_append_should_overwrite_after_delete[FwPointersCfg.DISABLED] _______
library = <VersionStore at 0x7fa61e4899b0>
    <ArcticLibrary at 0x7fa61e6c39b0, arctic_test.TEST>
        <Arctic at 0x7fa61e389278, connected to MongoClient(host=['127.12.101.44:12944'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_should_overwrite_after_delete(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.append(symbol, ts1, upsert=True)
            library.append(symbol, ts1_append, upsert=True)
            assert len(library.read(symbol).data) == len(ts1) + len(ts1_append)
>           library.delete(symbol)
tests/integration/store/test_version_store.py:337: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_append_should_overwrite_after_delete[FwPointersCfg.HYBRID] ________
library = <VersionStore at 0x7fa61c3aa908>
    <ArcticLibrary at 0x7fa61c3aa208, arctic_test.TEST>
        <Arctic at 0x7fa61c3aa6a0, connected to MongoClient(host=['127.12.101.44:1701'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_should_overwrite_after_delete(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.append(symbol, ts1, upsert=True)
            library.append(symbol, ts1_append, upsert=True)
            assert len(library.read(symbol).data) == len(ts1) + len(ts1_append)
>           library.delete(symbol)
tests/integration/store/test_version_store.py:337: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_append_should_overwrite_after_delete[FwPointersCfg.ENABLED] _______
library = <VersionStore at 0x7fa61c443ba8>
    <ArcticLibrary at 0x7fa61c443ac8, arctic_test.TEST>
        <Arctic at 0x7fa61c443b38, connected to MongoClient(host=['127.12.101.44:10997'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_append_should_overwrite_after_delete(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.append(symbol, ts1, upsert=True)
            library.append(symbol, ts1_append, upsert=True)
            assert len(library.read(symbol).data) == len(ts1) + len(ts1_append)
>           library.delete(symbol)
tests/integration/store/test_version_store.py:337: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________________ test_list_version_deleted ___________________________
library = <VersionStore at 0x7fa61e33d860>
    <ArcticLibrary at 0x7fa61e33d320, arctic_test.TEST>
        <Arctic at 0x7fa61e1fe0f0, connected to MongoClient(host=['127.12.101.44:10841'], document_class=dict, tz_aware=False, connect=True)>
    def test_list_version_deleted(library):
        assert len(library.list_versions(symbol)) == 0
        library.write(symbol, ts1, prune_previous_version=False)
        assert len(library.list_versions(symbol)) == 1
        # Snapshot the library so we keep the sentinel version
        library.snapshot('xxx', versions={symbol: 1})
>       library.delete(symbol)
tests/integration/store/test_version_store.py:408: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_delete_bson_versions[FwPointersCfg.DISABLED] _______________
library = <VersionStore at 0x7fa61e2f5400>
    <ArcticLibrary at 0x7fa61e728cf8, arctic_test.TEST>
        <Arctic at 0x7fa61e38bc18, connected to MongoClient(host=['127.12.101.44:16746'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_bson_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
>           library.write(symbol, a)
tests/integration/store/test_version_store.py:505: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_delete_bson_versions[FwPointersCfg.HYBRID] ________________
library = <VersionStore at 0x7fa61c382470>
    <ArcticLibrary at 0x7fa61c3826a0, arctic_test.TEST>
        <Arctic at 0x7fa61c6f0438, connected to MongoClient(host=['127.12.101.44:7222'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_bson_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
>           library.write(symbol, a)
tests/integration/store/test_version_store.py:505: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_delete_bson_versions[FwPointersCfg.ENABLED] _______________
library = <VersionStore at 0x7fa61c3b3908>
    <ArcticLibrary at 0x7fa61c3b3be0, arctic_test.TEST>
        <Arctic at 0x7fa61c3b3a20, connected to MongoClient(host=['127.12.101.44:31919'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_bson_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
>           library.write(symbol, a)
tests/integration/store/test_version_store.py:505: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_read_none_does_not_exception[FwPointersCfg.DISABLED] ___________
library = <VersionStore at 0x7fa61c6dda20>
    <ArcticLibrary at 0x7fa61c6dd4e0, arctic_test.TEST>
        <Arctic at 0x7fa61e1edef0, connected to MongoClient(host=['127.12.101.44:13304'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_read_none_does_not_exception(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write(symbol, None)
tests/integration/store/test_version_store.py:532: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_read_none_does_not_exception[FwPointersCfg.HYBRID] ____________
library = <VersionStore at 0x7fa61c769be0>
    <ArcticLibrary at 0x7fa61c769320, arctic_test.TEST>
        <Arctic at 0x7fa61c3a05c0, connected to MongoClient(host=['127.12.101.44:22925'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_read_none_does_not_exception(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write(symbol, None)
tests/integration/store/test_version_store.py:532: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_read_none_does_not_exception[FwPointersCfg.ENABLED] ___________
library = <VersionStore at 0x7fa61e1c98d0>
    <ArcticLibrary at 0x7fa61e1c9ba8, arctic_test.TEST>
        <Arctic at 0x7fa61e1c9a20, connected to MongoClient(host=['127.12.101.44:29488'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_read_none_does_not_exception(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write(symbol, None)
tests/integration/store/test_version_store.py:532: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_delete_item_has_symbol[FwPointersCfg.DISABLED] ______________
library = <VersionStore at 0x7fa61c6d2a20>
    <ArcticLibrary at 0x7fa61c6d2438, arctic_test.TEST>
        <Arctic at 0x7fa61e1d44a8, connected to MongoClient(host=['127.12.101.44:30598'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_item_has_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1)
            library.write(symbol, ts2, prune_previous_version=False)
            library.write(symbol, ts1, prune_previous_version=False)
            library.write(symbol, ts2, prune_previous_version=False)
    
>           library.delete(symbol)
tests/integration/store/test_version_store.py:544: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_delete_item_has_symbol[FwPointersCfg.HYBRID] _______________
library = <VersionStore at 0x7fa61e1cfba8>
    <ArcticLibrary at 0x7fa61e1cfcc0, arctic_test.TEST>
        <Arctic at 0x7fa61e1cf860, connected to MongoClient(host=['127.12.101.44:21518'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_item_has_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1)
            library.write(symbol, ts2, prune_previous_version=False)
            library.write(symbol, ts1, prune_previous_version=False)
            library.write(symbol, ts2, prune_previous_version=False)
    
>           library.delete(symbol)
tests/integration/store/test_version_store.py:544: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_delete_item_has_symbol[FwPointersCfg.ENABLED] ______________
library = <VersionStore at 0x7fa61c6a7748>
    <ArcticLibrary at 0x7fa61c6a71d0, arctic_test.TEST>
        <Arctic at 0x7fa61c6a77b8, connected to MongoClient(host=['127.12.101.44:6103'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_item_has_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1)
            library.write(symbol, ts2, prune_previous_version=False)
            library.write(symbol, ts1, prune_previous_version=False)
            library.write(symbol, ts2, prune_previous_version=False)
    
>           library.delete(symbol)
tests/integration/store/test_version_store.py:544: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______________ test_delete_item_snapshot[FwPointersCfg.DISABLED] _______________
library = <VersionStore at 0x7fa61c3e10b8>
    <ArcticLibrary at 0x7fa61c3e1358, arctic_test.TEST>
        <Arctic at 0x7fa61c3e1630, connected to MongoClient(host=['127.12.101.44:21917'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_item_snapshot(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1)
            library.write(symbol, ts2, prune_previous_version=False)
            library.write(symbol, ts1, prune_previous_version=False)
            library.snapshot('snap')
            library.write(symbol, ts2, prune_previous_version=False)
    
>           library.delete(symbol)
tests/integration/store/test_version_store.py:564: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_delete_item_snapshot[FwPointersCfg.HYBRID] ________________
library = <VersionStore at 0x7fa61c6bbf60>
    <ArcticLibrary at 0x7fa61c789cf8, arctic_test.TEST>
        <Arctic at 0x7fa61c6bb5c0, connected to MongoClient(host=['127.12.101.44:16928'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_item_snapshot(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1)
            library.write(symbol, ts2, prune_previous_version=False)
            library.write(symbol, ts1, prune_previous_version=False)
            library.snapshot('snap')
            library.write(symbol, ts2, prune_previous_version=False)
    
>           library.delete(symbol)
tests/integration/store/test_version_store.py:564: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_delete_item_snapshot[FwPointersCfg.ENABLED] _______________
library = <VersionStore at 0x7fa61e095cf8>
    <ArcticLibrary at 0x7fa61e095da0, arctic_test.TEST>
        <Arctic at 0x7fa61e095f28, connected to MongoClient(host=['127.12.101.44:31353'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_delete_item_snapshot(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.write(symbol, ts1)
            library.write(symbol, ts2, prune_previous_version=False)
            library.write(symbol, ts1, prune_previous_version=False)
            library.snapshot('snap')
            library.write(symbol, ts2, prune_previous_version=False)
    
>           library.delete(symbol)
tests/integration/store/test_version_store.py:564: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_prunes_multiple_versions[FwPointersCfg.DISABLED] _____________
library = <VersionStore at 0x7fa61c6b2e48>
    <ArcticLibrary at 0x7fa61e7964e0, arctic_test.TEST>
        <Arctic at 0x7fa61c6b2dd8, connected to MongoClient(host=['127.12.101.44:13868'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_prunes_multiple_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
            # Create an ObjectId
            now = dt.utcnow()
            with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
>               library.write(symbol, a, prune_previous_version=False)
tests/integration/store/test_version_store.py:765: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_prunes_multiple_versions[FwPointersCfg.HYBRID] ______________
library = <VersionStore at 0x7fa61c55bd30>
    <ArcticLibrary at 0x7fa61c55b0b8, arctic_test.TEST>
        <Arctic at 0x7fa61c55b550, connected to MongoClient(host=['127.12.101.44:32075'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_prunes_multiple_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
            # Create an ObjectId
            now = dt.utcnow()
            with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
>               library.write(symbol, a, prune_previous_version=False)
tests/integration/store/test_version_store.py:765: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_prunes_multiple_versions[FwPointersCfg.ENABLED] _____________
library = <VersionStore at 0x7fa61c3e3390>
    <ArcticLibrary at 0x7fa61c3e3588, arctic_test.TEST>
        <Arctic at 0x7fa61c546470, connected to MongoClient(host=['127.12.101.44:20606'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_prunes_multiple_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
            # Create an ObjectId
            now = dt.utcnow()
            with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
>               library.write(symbol, a, prune_previous_version=False)
tests/integration/store/test_version_store.py:765: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_prunes_doesnt_prune_snapshots[FwPointersCfg.DISABLED] __________
library = <VersionStore at 0x7fa61c37e588>
    <ArcticLibrary at 0x7fa61c37e080, arctic_test.TEST>
        <Arctic at 0x7fa61c37e908, connected to MongoClient(host=['127.12.101.44:30885'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_prunes_doesnt_prune_snapshots(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
            now = dt.utcnow()
            with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
>               library.write(symbol, a, prune_previous_version=False)
tests/integration/store/test_version_store.py:791: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_prunes_doesnt_prune_snapshots[FwPointersCfg.HYBRID] ___________
library = <VersionStore at 0x7fa61c261940>
    <ArcticLibrary at 0x7fa61c261b00, arctic_test.TEST>
        <Arctic at 0x7fa61c261278, connected to MongoClient(host=['127.12.101.44:18946'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_prunes_doesnt_prune_snapshots(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
            now = dt.utcnow()
            with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
>               library.write(symbol, a, prune_previous_version=False)
tests/integration/store/test_version_store.py:791: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_prunes_doesnt_prune_snapshots[FwPointersCfg.ENABLED] ___________
library = <VersionStore at 0x7fa61c56c780>
    <ArcticLibrary at 0x7fa61c56c128, arctic_test.TEST>
        <Arctic at 0x7fa61c3ca518, connected to MongoClient(host=['127.12.101.44:4487'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_prunes_doesnt_prune_snapshots(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            coll = library._collection
    
            a = [{'a': 'b'}]
            c = [{'c': 'd'}]
            now = dt.utcnow()
            with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
>               library.write(symbol, a, prune_previous_version=False)
tests/integration/store/test_version_store.py:791: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = [{'a': 'b'}]
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________________ test_list_symbols[FwPointersCfg.DISABLED] ___________________
library = <VersionStore at 0x7fa61e0217b8>
    <ArcticLibrary at 0x7fa61e0215c0, arctic_test.TEST>
        <Arctic at 0x7fa61e13ff28, connected to MongoClient(host=['127.12.101.44:1808'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.snapshot('snap1')
>           library.write('asdf', {'foo': 'bar'}, metadata={'a': 1, 'b': 10})
tests/integration/store/test_version_store.py:1029: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________________ test_list_symbols[FwPointersCfg.HYBRID] ____________________
library = <VersionStore at 0x7fa61d879d30>
    <ArcticLibrary at 0x7fa61c7890f0, arctic_test.TEST>
        <Arctic at 0x7fa61d879f28, connected to MongoClient(host=['127.12.101.44:5677'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.snapshot('snap1')
>           library.write('asdf', {'foo': 'bar'}, metadata={'a': 1, 'b': 10})
tests/integration/store/test_version_store.py:1029: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________________ test_list_symbols[FwPointersCfg.ENABLED] ___________________
library = <VersionStore at 0x7fa61c5439b0>
    <ArcticLibrary at 0x7fa61c543630, arctic_test.TEST>
        <Arctic at 0x7fa61c543dd8, connected to MongoClient(host=['127.12.101.44:26373'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.snapshot('snap1')
>           library.write('asdf', {'foo': 'bar'}, metadata={'a': 1, 'b': 10})
tests/integration/store/test_version_store.py:1029: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______________ test_list_symbols_regex[FwPointersCfg.DISABLED] ________________
library = <VersionStore at 0x7fa61c2b3240>
    <ArcticLibrary at 0x7fa61c2b37b8, arctic_test.TEST>
        <Arctic at 0x7fa61c2b3828, connected to MongoClient(host=['127.12.101.44:22271'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_regex(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.snapshot('snap1')
>           library.write('asdf', {'foo': 'bar'}, metadata={'a': 1, 'b': 10})
tests/integration/store/test_version_store.py:1044: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________ test_list_symbols_regex[FwPointersCfg.HYBRID] _________________
library = <VersionStore at 0x7fa61c2b3160>
    <ArcticLibrary at 0x7fa61c2b3c88, arctic_test.TEST>
        <Arctic at 0x7fa61c2b3f98, connected to MongoClient(host=['127.12.101.44:18885'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_regex(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.snapshot('snap1')
>           library.write('asdf', {'foo': 'bar'}, metadata={'a': 1, 'b': 10})
tests/integration/store/test_version_store.py:1044: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________________ test_list_symbols_regex[FwPointersCfg.ENABLED] ________________
library = <VersionStore at 0x7fa61c647978>
    <ArcticLibrary at 0x7fa61c647160, arctic_test.TEST>
        <Arctic at 0x7fa61c2983c8, connected to MongoClient(host=['127.12.101.44:27123'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_regex(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            library.snapshot('snap1')
>           library.write('asdf', {'foo': 'bar'}, metadata={'a': 1, 'b': 10})
tests/integration/store/test_version_store.py:1044: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_list_symbols_newer_version_with_lower_id[FwPointersCfg.DISABLED] _____
library = <VersionStore at 0x7fa61c77f278>
    <ArcticLibrary at 0x7fa61c77fa90, arctic_test.TEST>
        <Arctic at 0x7fa61c77f518, connected to MongoClient(host=['127.12.101.44:9903'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_newer_version_with_lower_id(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            now = struct.pack(">i", int(time.time()))
            old_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x00")
            new_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x01")
            object_id_class = Mock()
            object_id_class.from_datetime = bson.ObjectId.from_datetime
    
            object_id_class.return_value = new_id
            with patch("bson.ObjectId", object_id_class):
                library.write(symbol, ts1)
    
            library.snapshot('s1')
    
            object_id_class.return_value = old_id
            with patch("bson.ObjectId", object_id_class):
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1077: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_list_symbols_newer_version_with_lower_id[FwPointersCfg.HYBRID] ______
library = <VersionStore at 0x7fa61c7d87f0>
    <ArcticLibrary at 0x7fa61c7d8b70, arctic_test.TEST>
        <Arctic at 0x7fa61c7d8cf8, connected to MongoClient(host=['127.12.101.44:20369'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_newer_version_with_lower_id(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            now = struct.pack(">i", int(time.time()))
            old_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x00")
            new_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x01")
            object_id_class = Mock()
            object_id_class.from_datetime = bson.ObjectId.from_datetime
    
            object_id_class.return_value = new_id
            with patch("bson.ObjectId", object_id_class):
                library.write(symbol, ts1)
    
            library.snapshot('s1')
    
            object_id_class.return_value = old_id
            with patch("bson.ObjectId", object_id_class):
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1077: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_list_symbols_newer_version_with_lower_id[FwPointersCfg.ENABLED] _____
library = <VersionStore at 0x7fa630762b38>
    <ArcticLibrary at 0x7fa6307627b8, arctic_test.TEST>
        <Arctic at 0x7fa61c7cc978, connected to MongoClient(host=['127.12.101.44:28259'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_newer_version_with_lower_id(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            now = struct.pack(">i", int(time.time()))
            old_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x00")
            new_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x01")
            object_id_class = Mock()
            object_id_class.from_datetime = bson.ObjectId.from_datetime
    
            object_id_class.return_value = new_id
            with patch("bson.ObjectId", object_id_class):
                library.write(symbol, ts1)
    
            library.snapshot('s1')
    
            object_id_class.return_value = old_id
            with patch("bson.ObjectId", object_id_class):
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1077: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_list_symbols_write_snapshot_write_delete[FwPointersCfg.DISABLED] _____
library = <VersionStore at 0x7fa61c7833c8>
    <ArcticLibrary at 0x7fa61c783c18, arctic_test.TEST>
        <Arctic at 0x7fa61c7ea358, connected to MongoClient(host=['127.12.101.44:21814'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_write_snapshot_write_delete(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write('asdf', {'foo': 'bar'})
tests/integration/store/test_version_store.py:1085: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_list_symbols_write_snapshot_write_delete[FwPointersCfg.HYBRID] ______
library = <VersionStore at 0x7fa61c296ac8>
    <ArcticLibrary at 0x7fa61c296898, arctic_test.TEST>
        <Arctic at 0x7fa61c23f0f0, connected to MongoClient(host=['127.12.101.44:11693'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_write_snapshot_write_delete(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write('asdf', {'foo': 'bar'})
tests/integration/store/test_version_store.py:1085: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_list_symbols_write_snapshot_write_delete[FwPointersCfg.ENABLED] _____
library = <VersionStore at 0x7fa61e168ac8>
    <ArcticLibrary at 0x7fa61e168550, arctic_test.TEST>
        <Arctic at 0x7fa61e168898, connected to MongoClient(host=['127.12.101.44:14880'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_write_snapshot_write_delete(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write('asdf', {'foo': 'bar'})
tests/integration/store/test_version_store.py:1085: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_list_symbols_delete_write[FwPointersCfg.DISABLED] ____________
library = <VersionStore at 0x7fa61c669400>
    <ArcticLibrary at 0x7fa61c669b70, arctic_test.TEST>
        <Arctic at 0x7fa61c613ef0, connected to MongoClient(host=['127.12.101.44:8895'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_delete_write(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'sym_a'
>           library.write(symbol, {'foo': 'bar2'}, prune_previous_version=False)
tests/integration/store/test_version_store.py:1101: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar2'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_list_symbols_delete_write[FwPointersCfg.HYBRID] _____________
library = <VersionStore at 0x7fa61c263438>
    <ArcticLibrary at 0x7fa61c2638d0, arctic_test.TEST>
        <Arctic at 0x7fa61c263048, connected to MongoClient(host=['127.12.101.44:11254'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_delete_write(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'sym_a'
>           library.write(symbol, {'foo': 'bar2'}, prune_previous_version=False)
tests/integration/store/test_version_store.py:1101: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar2'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_list_symbols_delete_write[FwPointersCfg.ENABLED] _____________
library = <VersionStore at 0x7fa61c6f56d8>
    <ArcticLibrary at 0x7fa61e684470, arctic_test.TEST>
        <Arctic at 0x7fa61c590048, connected to MongoClient(host=['127.12.101.44:1400'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_list_symbols_delete_write(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'sym_a'
>           library.write(symbol, {'foo': 'bar2'}, prune_previous_version=False)
tests/integration/store/test_version_store.py:1101: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = {'foo': 'bar2'}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_write_metadata_new_symbol[FwPointersCfg.DISABLED] ____________
self = <VersionStore at 0x7fa61c790978>
    <ArcticLibrary at 0x7fa61e095208, arctic_test.TEST>
        <Arctic at 0x7fa61e7b0ef0, connected to MongoClient(host=['127.12.101.44:10489'], document_class=dict, tz_aware=False, connect=True)>
symbol = 'FTL', metadata = {'field_b': 1}, prune_previous_version = True
kwargs = {}
    @mongo_retry
    def write_metadata(self, symbol, metadata, prune_previous_version=True, **kwargs):
        """
        Write 'metadata' under the specified 'symbol' name to this library.
        The data will remain unchanged. A new version will be created.
        If the symbol is missing, it causes a write with empty data (None, pickled, can't append)
        and the supplied metadata.
        Returns a VersionedItem object only with a metadata element.
        Fast operation: Zero data/segment read/write operations.
    
        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict` or `None`
            dictionary of metadata to persist along with the symbol
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True
        kwargs :
            passed through to the write handler (only used if symbol does not already exist or is deleted)
    
        Returns
        -------
        `VersionedItem`
            VersionedItem named tuple containing the metadata of the written symbol's version document in the store.
        """
        # Make a normal write with empty data and supplied metadata if symbol does not exist
        try:
>           previous_version = self._read_metadata(symbol)
arctic/store/version_store.py:752: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
self = <VersionStore at 0x7fa61c790978>
    <ArcticLibrary at 0x7fa61e095208, arctic_test.TEST>
        <Arctic at 0x7fa61e7b0ef0, connected to MongoClient(host=['127.12.101.44:10489'], document_class=dict, tz_aware=False, connect=True)>
symbol = 'FTL', as_of = None
read_preference = PrimaryPreferred(tag_sets=None, max_staleness=-1, hedge=None)
    def _read_metadata(self, symbol, as_of=None, read_preference=None):
        if read_preference is None:
            # We want to hit the PRIMARY if querying secondaries is disabled.  If we're allowed to query secondaries,
            # then we want to hit the secondary for metadata.  We maintain ordering of chunks vs. metadata, such that
            # if metadata is available, we guarantee that chunks will be available. (Within a 10 minute window.)
            read_preference = ReadPreference.PRIMARY_PREFERRED if not self._allow_secondary else ReadPreference.SECONDARY_PREFERRED
    
        versions_coll = self._versions.with_options(read_preference=read_preference)
    
        _version = None
        if as_of is None:
            _version = versions_coll.find_one({'symbol': symbol}, sort=[('version', pymongo.DESCENDING)])
        elif isinstance(as_of, six.string_types):
            # as_of is a snapshot
            snapshot = self._snapshots.find_one({'name': as_of})
            if snapshot:
                _version = versions_coll.find_one({'symbol': symbol, 'parent': snapshot['_id']})
        elif isinstance(as_of, dt):
            # as_of refers to a datetime
            if not as_of.tzinfo:
                as_of = as_of.replace(tzinfo=mktz())
            _version = versions_coll.find_one({'symbol': symbol,
                                               '_id': {'$lt': bson.ObjectId.from_datetime(as_of + timedelta(seconds=1))}},
                                              sort=[('symbol', pymongo.DESCENDING), ('version', pymongo.DESCENDING)])
        else:
            # Backward compatibility - as of is a version number
            _version = versions_coll.find_one({'symbol': symbol, 'version': as_of})
    
        if not _version:
>           raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))
E           arctic.exceptions.NoDataFoundException: No data found for FTL in library arctic_test.TEST
arctic/store/version_store.py:514: NoDataFoundException
During handling of the above exception, another exception occurred:
library = <VersionStore at 0x7fa61c790978>
    <ArcticLibrary at 0x7fa61e095208, arctic_test.TEST>
        <Arctic at 0x7fa61e7b0ef0, connected to MongoClient(host=['127.12.101.44:10489'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_new_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            with patch('arctic.arctic.logger.info') as info:
>               library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 1 (only metadata)
tests/integration/store/test_version_store.py:1194: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:755: in write_metadata
    prune_previous_version=prune_previous_version, **kwargs)
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____________ test_write_metadata_new_symbol[FwPointersCfg.HYBRID] _____________
self = <VersionStore at 0x7fa5fcf3f0f0>
    <ArcticLibrary at 0x7fa5fcf3f780, arctic_test.TEST>
        <Arctic at 0x7fa61c2043c8, connected to MongoClient(host=['127.12.101.44:6872'], document_class=dict, tz_aware=False, connect=True)>
symbol = 'FTL', metadata = {'field_b': 1}, prune_previous_version = True
kwargs = {}
    @mongo_retry
    def write_metadata(self, symbol, metadata, prune_previous_version=True, **kwargs):
        """
        Write 'metadata' under the specified 'symbol' name to this library.
        The data will remain unchanged. A new version will be created.
        If the symbol is missing, it causes a write with empty data (None, pickled, can't append)
        and the supplied metadata.
        Returns a VersionedItem object only with a metadata element.
        Fast operation: Zero data/segment read/write operations.
    
        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict` or `None`
            dictionary of metadata to persist along with the symbol
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True
        kwargs :
            passed through to the write handler (only used if symbol does not already exist or is deleted)
    
        Returns
        -------
        `VersionedItem`
            VersionedItem named tuple containing the metadata of the written symbol's version document in the store.
        """
        # Make a normal write with empty data and supplied metadata if symbol does not exist
        try:
>           previous_version = self._read_metadata(symbol)
arctic/store/version_store.py:752: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
self = <VersionStore at 0x7fa5fcf3f0f0>
    <ArcticLibrary at 0x7fa5fcf3f780, arctic_test.TEST>
        <Arctic at 0x7fa61c2043c8, connected to MongoClient(host=['127.12.101.44:6872'], document_class=dict, tz_aware=False, connect=True)>
symbol = 'FTL', as_of = None
read_preference = PrimaryPreferred(tag_sets=None, max_staleness=-1, hedge=None)
    def _read_metadata(self, symbol, as_of=None, read_preference=None):
        if read_preference is None:
            # We want to hit the PRIMARY if querying secondaries is disabled.  If we're allowed to query secondaries,
            # then we want to hit the secondary for metadata.  We maintain ordering of chunks vs. metadata, such that
            # if metadata is available, we guarantee that chunks will be available. (Within a 10 minute window.)
            read_preference = ReadPreference.PRIMARY_PREFERRED if not self._allow_secondary else ReadPreference.SECONDARY_PREFERRED
    
        versions_coll = self._versions.with_options(read_preference=read_preference)
    
        _version = None
        if as_of is None:
            _version = versions_coll.find_one({'symbol': symbol}, sort=[('version', pymongo.DESCENDING)])
        elif isinstance(as_of, six.string_types):
            # as_of is a snapshot
            snapshot = self._snapshots.find_one({'name': as_of})
            if snapshot:
                _version = versions_coll.find_one({'symbol': symbol, 'parent': snapshot['_id']})
        elif isinstance(as_of, dt):
            # as_of refers to a datetime
            if not as_of.tzinfo:
                as_of = as_of.replace(tzinfo=mktz())
            _version = versions_coll.find_one({'symbol': symbol,
                                               '_id': {'$lt': bson.ObjectId.from_datetime(as_of + timedelta(seconds=1))}},
                                              sort=[('symbol', pymongo.DESCENDING), ('version', pymongo.DESCENDING)])
        else:
            # Backward compatibility - as of is a version number
            _version = versions_coll.find_one({'symbol': symbol, 'version': as_of})
    
        if not _version:
>           raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))
E           arctic.exceptions.NoDataFoundException: No data found for FTL in library arctic_test.TEST
arctic/store/version_store.py:514: NoDataFoundException
During handling of the above exception, another exception occurred:
library = <VersionStore at 0x7fa5fcf3f0f0>
    <ArcticLibrary at 0x7fa5fcf3f780, arctic_test.TEST>
        <Arctic at 0x7fa61c2043c8, connected to MongoClient(host=['127.12.101.44:6872'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_new_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            with patch('arctic.arctic.logger.info') as info:
>               library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 1 (only metadata)
tests/integration/store/test_version_store.py:1194: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:755: in write_metadata
    prune_previous_version=prune_previous_version, **kwargs)
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____________ test_write_metadata_new_symbol[FwPointersCfg.ENABLED] _____________
self = <VersionStore at 0x7fa61c204e80>
    <ArcticLibrary at 0x7fa61c2041d0, arctic_test.TEST>
        <Arctic at 0x7fa5fcf92160, connected to MongoClient(host=['127.12.101.44:20668'], document_class=dict, tz_aware=False, connect=True)>
symbol = 'FTL', metadata = {'field_b': 1}, prune_previous_version = True
kwargs = {}
    @mongo_retry
    def write_metadata(self, symbol, metadata, prune_previous_version=True, **kwargs):
        """
        Write 'metadata' under the specified 'symbol' name to this library.
        The data will remain unchanged. A new version will be created.
        If the symbol is missing, it causes a write with empty data (None, pickled, can't append)
        and the supplied metadata.
        Returns a VersionedItem object only with a metadata element.
        Fast operation: Zero data/segment read/write operations.
    
        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict` or `None`
            dictionary of metadata to persist along with the symbol
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True
        kwargs :
            passed through to the write handler (only used if symbol does not already exist or is deleted)
    
        Returns
        -------
        `VersionedItem`
            VersionedItem named tuple containing the metadata of the written symbol's version document in the store.
        """
        # Make a normal write with empty data and supplied metadata if symbol does not exist
        try:
>           previous_version = self._read_metadata(symbol)
arctic/store/version_store.py:752: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
self = <VersionStore at 0x7fa61c204e80>
    <ArcticLibrary at 0x7fa61c2041d0, arctic_test.TEST>
        <Arctic at 0x7fa5fcf92160, connected to MongoClient(host=['127.12.101.44:20668'], document_class=dict, tz_aware=False, connect=True)>
symbol = 'FTL', as_of = None
read_preference = PrimaryPreferred(tag_sets=None, max_staleness=-1, hedge=None)
    def _read_metadata(self, symbol, as_of=None, read_preference=None):
        if read_preference is None:
            # We want to hit the PRIMARY if querying secondaries is disabled.  If we're allowed to query secondaries,
            # then we want to hit the secondary for metadata.  We maintain ordering of chunks vs. metadata, such that
            # if metadata is available, we guarantee that chunks will be available. (Within a 10 minute window.)
            read_preference = ReadPreference.PRIMARY_PREFERRED if not self._allow_secondary else ReadPreference.SECONDARY_PREFERRED
    
        versions_coll = self._versions.with_options(read_preference=read_preference)
    
        _version = None
        if as_of is None:
            _version = versions_coll.find_one({'symbol': symbol}, sort=[('version', pymongo.DESCENDING)])
        elif isinstance(as_of, six.string_types):
            # as_of is a snapshot
            snapshot = self._snapshots.find_one({'name': as_of})
            if snapshot:
                _version = versions_coll.find_one({'symbol': symbol, 'parent': snapshot['_id']})
        elif isinstance(as_of, dt):
            # as_of refers to a datetime
            if not as_of.tzinfo:
                as_of = as_of.replace(tzinfo=mktz())
            _version = versions_coll.find_one({'symbol': symbol,
                                               '_id': {'$lt': bson.ObjectId.from_datetime(as_of + timedelta(seconds=1))}},
                                              sort=[('symbol', pymongo.DESCENDING), ('version', pymongo.DESCENDING)])
        else:
            # Backward compatibility - as of is a version number
            _version = versions_coll.find_one({'symbol': symbol, 'version': as_of})
    
        if not _version:
>           raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))
E           arctic.exceptions.NoDataFoundException: No data found for FTL in library arctic_test.TEST
arctic/store/version_store.py:514: NoDataFoundException
During handling of the above exception, another exception occurred:
library = <VersionStore at 0x7fa61c204e80>
    <ArcticLibrary at 0x7fa61c2041d0, arctic_test.TEST>
        <Arctic at 0x7fa5fcf92160, connected to MongoClient(host=['127.12.101.44:20668'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_new_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            with patch('arctic.arctic.logger.info') as info:
>               library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 1 (only metadata)
tests/integration/store/test_version_store.py:1194: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:755: in write_metadata
    prune_previous_version=prune_previous_version, **kwargs)
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED] ______
library = <VersionStore at 0x7fa61c3b71d0>
    <ArcticLibrary at 0x7fa61e35edd8, arctic_test.TEST>
        <Arctic at 0x7fa61e0bedd8, connected to MongoClient(host=['127.12.101.44:6814'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_purge_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                with FwPointersCtx(fw_pointers_cfg):
                    library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                    library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                    assert library._read_metadata(symbol).get('version') == 2
                    library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                    # Trigger GC now
                    library._prune_previous_versions(symbol, 0)
                    time.sleep(2)
    
                    # Assert the data
                    v = library.read(symbol)
                    assert v.data.equals(mydf_b)    # FIXME: CM#009 - (replace assert_frame_equal with df.equals)
                    assert v.metadata == {'field_b': 1}
    
                    # Check if after snapshot and deleting the symbol, the data/metadata survive
                    library.snapshot('SNAP_1')
>                   library.delete(symbol)
tests/integration/store/test_version_store.py:1239: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID] _______
library = <VersionStore at 0x7fa61c182518>
    <ArcticLibrary at 0x7fa61c182f60, arctic_test.TEST>
        <Arctic at 0x7fa61c12d3c8, connected to MongoClient(host=['127.12.101.44:1945'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_purge_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                with FwPointersCtx(fw_pointers_cfg):
                    library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                    library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                    assert library._read_metadata(symbol).get('version') == 2
                    library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                    # Trigger GC now
                    library._prune_previous_versions(symbol, 0)
                    time.sleep(2)
    
                    # Assert the data
                    v = library.read(symbol)
                    assert v.data.equals(mydf_b)    # FIXME: CM#009 - (replace assert_frame_equal with df.equals)
                    assert v.metadata == {'field_b': 1}
    
                    # Check if after snapshot and deleting the symbol, the data/metadata survive
                    library.snapshot('SNAP_1')
>                   library.delete(symbol)
tests/integration/store/test_version_store.py:1239: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

______ test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED] ______
library = <VersionStore at 0x7fa5fddb7588>
    <ArcticLibrary at 0x7fa5fddb7c88, arctic_test.TEST>
        <Arctic at 0x7fa5fddb71d0, connected to MongoClient(host=['127.12.101.44:31770'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_purge_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                with FwPointersCtx(fw_pointers_cfg):
                    library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                    library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                    assert library._read_metadata(symbol).get('version') == 2
                    library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                    # Trigger GC now
                    library._prune_previous_versions(symbol, 0)
                    time.sleep(2)
    
                    # Assert the data
                    v = library.read(symbol)
                    assert v.data.equals(mydf_b)    # FIXME: CM#009 - (replace assert_frame_equal with df.equals)
                    assert v.metadata == {'field_b': 1}
    
                    # Check if after snapshot and deleting the symbol, the data/metadata survive
                    library.snapshot('SNAP_1')
>                   library.delete(symbol)
tests/integration/store/test_version_store.py:1239: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

__________ test_write_metadata_delete_symbol[FwPointersCfg.DISABLED] ___________
library = <VersionStore at 0x7fa61c0a6828>
    <ArcticLibrary at 0x7fa61c0a6cf8, arctic_test.TEST>
        <Arctic at 0x7fa61c0a62e8, connected to MongoClient(host=['127.12.101.44:19801'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_delete_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
    
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1256: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_write_metadata_delete_symbol[FwPointersCfg.HYBRID] ____________
library = <VersionStore at 0x7fa5fceffef0>
    <ArcticLibrary at 0x7fa5fceff860, arctic_test.TEST>
        <Arctic at 0x7fa61c0a6860, connected to MongoClient(host=['127.12.101.44:6478'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_delete_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
    
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1256: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___________ test_write_metadata_delete_symbol[FwPointersCfg.ENABLED] ___________
library = <VersionStore at 0x7fa5fcebc908>
    <ArcticLibrary at 0x7fa5fcefff60, arctic_test.TEST>
        <Arctic at 0x7fa5fcebc358, connected to MongoClient(host=['127.12.101.44:26344'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_delete_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
    
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1256: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

___ test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED] ____
library = <VersionStore at 0x7fa61c298b00>
    <ArcticLibrary at 0x7fa61c2987f0, arctic_test.TEST>
        <Arctic at 0x7fa61c5115f8, connected to MongoClient(host=['127.12.101.44:27800'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_snap_delete_symbol_restore(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf = _rnd_df(20, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf[:10], metadata={'field_a': 1})  # creates version 1
                library.append(symbol, data=mydf[10:15])  # version 2
                library.snapshot('snapA')
    
                library.append(symbol, data=mydf[15:20])  # version 3
>               library.delete(symbol)  # version 4
tests/integration/store/test_version_store.py:1482: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID] _____
library = <VersionStore at 0x7fa5fcc71da0>
    <ArcticLibrary at 0x7fa5fdf9cc18, arctic_test.TEST>
        <Arctic at 0x7fa5fdf9ca90, connected to MongoClient(host=['127.12.101.44:1613'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_snap_delete_symbol_restore(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf = _rnd_df(20, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf[:10], metadata={'field_a': 1})  # creates version 1
                library.append(symbol, data=mydf[10:15])  # version 2
                library.snapshot('snapA')
    
                library.append(symbol, data=mydf[15:20])  # version 3
>               library.delete(symbol)  # version 4
tests/integration/store/test_version_store.py:1482: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED] ____
library = <VersionStore at 0x7fa5fcfa1b70>
    <ArcticLibrary at 0x7fa5fcfa1f28, arctic_test.TEST>
        <Arctic at 0x7fa5fdf46860, connected to MongoClient(host=['127.12.101.44:6750'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_snap_delete_symbol_restore(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf = _rnd_df(20, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf[:10], metadata={'field_a': 1})  # creates version 1
                library.append(symbol, data=mydf[10:15])  # version 2
                library.snapshot('snapA')
    
                library.append(symbol, data=mydf[15:20])  # version 3
>               library.delete(symbol)  # version 4
tests/integration/store/test_version_store.py:1482: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

____ test_restore_from_version_with_deleted_symbol[FwPointersCfg.DISABLED] _____
library = <VersionStore at 0x7fa61c523a20>
    <ArcticLibrary at 0x7fa61c523c50, arctic_test.TEST>
        <Arctic at 0x7fa5fdf8dba8, connected to MongoClient(host=['127.12.101.44:12417'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_from_version_with_deleted_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1501: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_restore_from_version_with_deleted_symbol[FwPointersCfg.HYBRID] ______
library = <VersionStore at 0x7fa5fdefd898>
    <ArcticLibrary at 0x7fa5fdefd278, arctic_test.TEST>
        <Arctic at 0x7fa5fcc45eb8, connected to MongoClient(host=['127.12.101.44:13047'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_from_version_with_deleted_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1501: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_restore_from_version_with_deleted_symbol[FwPointersCfg.ENABLED] _____
library = <VersionStore at 0x7fa61c7ba860>
    <ArcticLibrary at 0x7fa61c7baac8, arctic_test.TEST>
        <Arctic at 0x7fa61c21f588, connected to MongoClient(host=['127.12.101.44:30400'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_from_version_with_deleted_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
>               library.delete(symbol)
tests/integration/store/test_version_store.py:1501: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:940: in delete
    sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = None
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_snapshot_list_versions_after_delete[FwPointersCfg.DISABLED] _______
library = <VersionStore at 0x7fa61c5845c0>
    <ArcticLibrary at 0x7fa61c584eb8, arctic_test.TEST>
        <Arctic at 0x7fa61c584208, connected to MongoClient(host=['127.12.101.44:6353'], document_class=dict, tz_aware=False, connect=True)>
library_name = 'test.TEST', fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_snapshot_list_versions_after_delete(library, library_name, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write("symA", 'data data')
tests/integration/store/test_version_store.py:1607: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'data data'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

________ test_snapshot_list_versions_after_delete[FwPointersCfg.HYBRID] ________
library = <VersionStore at 0x7fa5fdf345f8>
    <ArcticLibrary at 0x7fa5fdf34080, arctic_test.TEST>
        <Arctic at 0x7fa61c5840f0, connected to MongoClient(host=['127.12.101.44:22475'], document_class=dict, tz_aware=False, connect=True)>
library_name = 'test.TEST', fw_pointers_cfg = <FwPointersCfg.HYBRID: 2>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_snapshot_list_versions_after_delete(library, library_name, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write("symA", 'data data')
tests/integration/store/test_version_store.py:1607: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'data data'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_______ test_snapshot_list_versions_after_delete[FwPointersCfg.ENABLED] ________
library = <VersionStore at 0x7fa5fceec6a0>
    <ArcticLibrary at 0x7fa5fceec438, arctic_test.TEST>
        <Arctic at 0x7fa5fdd6f400, connected to MongoClient(host=['127.12.101.44:1796'], document_class=dict, tz_aware=False, connect=True)>
library_name = 'test.TEST', fw_pointers_cfg = <FwPointersCfg.ENABLED: 0>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_snapshot_list_versions_after_delete(library, library_name, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
>           library.write("symA", 'data data')
tests/integration/store/test_version_store.py:1607: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data = 'data data'
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

_____ test_write_non_serializable_pickling_default[FwPointersCfg.DISABLED] _____
arctic = <Arctic at 0x7fa61e2b3978, connected to MongoClient(host=['127.12.101.44:2240'], document_class=dict, tz_aware=False, connect=True)>
fw_pointers_cfg = <FwPointersCfg.DISABLED: 1>
    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_non_serializable_pickling_default(arctic, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            lib_name = 'write_hanlder_test'
            arctic.initialize_library(lib_name, VERSION_STORE)
            library = arctic[lib_name]
            df = pd.DataFrame({'a': [dict(a=1)]})
>           library.write('ns3', df)
tests/integration/store/test_version_store.py:1641: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/decorators.py:50: in f_retry
    return f(*args, **kwargs)
arctic/store/version_store.py:661: in write
    handler = self._write_handler(version, symbol, data, **kwargs)
arctic/store/version_store.py:328: in _write_handler
    if h.can_write(version, symbol, data, **kwargs):
arctic/store/_pandas_ndarray_store.py:223: in can_write
    if self.can_write_type(data):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
data =           a
0  {'a': 1}
    @staticmethod
    def can_write_type(data):
>       return isinstance(data, Panel)
E       NameError: name 'Panel' is not defined
arctic/store/_pandas_ndarray_store.py:220: NameError

================================================================================

...

The job exceeded the maximum log length, and has been terminated
```