from pytest import fail


def test_save_read_version_doc(s3_store):
    version_doc = {'symbol': 24, 'foo': 'bar'}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    loaded_version_doc = s3_store.read_version(library_name='my_library', symbol='my_symbol')
    assert version_doc == loaded_version_doc


def test_read_a_specific_version_doc(s3_store):
    version_docs = [{'symbol': '000', 'foo': 'bar'}, {'symbol': '111', 'foo': 'bar'}]
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_docs[0])
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_docs[1])
    versions = s3_store.list_versions(library_name='my_library', symbol='my_symbol')

    for idx, row in versions.iterrows():
        # test read by version_id
        loaded_version_doc = s3_store.read_version(library_name='my_library',
                                                   symbol='my_symbol', version_id=row.VersionId)
        assert version_docs[idx] == loaded_version_doc
        # test read by as_of
        loaded_version_doc = s3_store.read_version(library_name='my_library',
                                                   symbol='my_symbol', as_of=row.LastModified)
        assert version_docs[idx] == loaded_version_doc


def test_save_read_segments(s3_store):
    segment_data = b'3424234235'
    segment_key = s3_store.write_segment(library_name='my_library', symbol='symbol', segment_data=segment_data)
    loaded_segment_data = list(s3_store.read_segments(library_name='my_library', segment_keys=[segment_key]))[0]
    assert segment_data == loaded_segment_data


def test_list_symbols(s3_store):
    version_doc = {'symbol': 24, 'foo': 'bar'}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    s3_store.write_version(library_name='my_library', symbol='my_symbol2', version_doc=version_doc)
    symbols = s3_store.list_symbols(library_name='my_library')
    assert ['my_symbol', 'my_symbol2'] == symbols


def test_delete_symbol(s3_store):
    version_doc = {'symbol': 24, 'foo': 'bar'}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    s3_store.write_version(library_name='my_library', symbol='my_symbol2', version_doc=version_doc)
    assert ['my_symbol', 'my_symbol2'] == s3_store.list_symbols(library_name='my_library')
    s3_store.delete_symbol(library_name='my_library', symbol='my_symbol')
    assert ['my_symbol2'] == s3_store.list_symbols(library_name='my_library')


def test_list_versions(s3_store):
    version_doc = {'symbol': 24, 'foo': 'bar'}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    versions = s3_store.list_versions(library_name='my_library', symbol='my_symbol')
    assert len(versions) == 2


def test_list_all_versions(s3_store):
    version_doc = {'symbol': 24, 'foo': 'bar'}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    s3_store.write_version(library_name='my_library', symbol='my_symbol2', version_doc=version_doc)
    versions = s3_store._list_all_versions(library_name='my_library')
    assert len(versions) == 2


def test_create_and_read_snapshot(s3_store):
    version_doc = {'symbol': 24, 'foo': 'bar'}
    latest_versions = {}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=version_doc)
    latest_versions['my_symbol'] = version_doc['version']
    s3_store.write_version(library_name='my_library', symbol='my_symbol2', version_doc=version_doc)
    latest_versions['my_symbol2'] = version_doc['version']
    s3_store.write_version(library_name='my_library', symbol='my_symbol3', version_doc=version_doc)
    metadata = {'month': 'June'}
    s3_store.snapshot(library_name='my_library', snap_name='snap1', metadata=metadata, skip_symbols=['my_symbol3'])
    snap = s3_store._read_snapshot(library_name='my_library', snap_name='snap1')
    assert snap['versions'] == latest_versions
    assert snap['metadata'] == metadata


def test_reading_from_snapshot(s3_store):
    my_symbol_version_doc_0 = {'foo': 24, 'data': 1}
    my_symbol_version_doc_1 = {'foo': 24, 'data': 2}
    my_symbol2_version_doc_0 = {'foo': 24, 'data': 999}
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=my_symbol_version_doc_0)
    s3_store.snapshot(library_name='my_library', snap_name='snap0')
    s3_store.write_version(library_name='my_library', symbol='my_symbol', version_doc=my_symbol_version_doc_1)
    s3_store.snapshot(library_name='my_library', snap_name='snap1')
    s3_store.write_version(library_name='my_library', symbol='my_symbol2', version_doc=my_symbol2_version_doc_0)
    s3_store.snapshot(library_name='my_library', snap_name='snap2')

    assert my_symbol_version_doc_0 == s3_store.read_version(library_name='my_library',
                                                            symbol='my_symbol', snapshot_id='snap0')
    assert my_symbol_version_doc_1 == s3_store.read_version(library_name='my_library',
                                                            symbol='my_symbol', snapshot_id='snap1')
    assert my_symbol2_version_doc_0 == s3_store.read_version(library_name='my_library',
                                                             symbol='my_symbol2', snapshot_id='snap2')

    try:
        s3_store.read_version(library_name='my_library', symbol='my_symbol2', snapshot_id='snap0')
        fail("Should not find symbol")
    except KeyError:
        pass

    # can delete a snapshot
    assert set(s3_store.list_snapshots(library_name='my_library')) == {'snap0', 'snap1', 'snap2'}
    s3_store.delete_snapshot('my_library', 'snap0')
    assert set(s3_store.list_snapshots(library_name='my_library')) == {'snap1', 'snap2'}

    # should be able to read a deleted symbol from a snap after deleting the symbol
    s3_store.delete_symbol(library_name='my_library', symbol='my_symbol2')
    assert my_symbol2_version_doc_0 == s3_store.read_version(library_name='my_library',
                                                             symbol='my_symbol2', snapshot_id='snap2')