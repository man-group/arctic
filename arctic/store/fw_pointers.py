
WITH_ID = 'fw_pointers_with_id'
WITH_SHA = 'fw_pointers_with_sha'
LEGACY = 'legacy'


def get_fw_pointers_type(version):
    fw_pointers_type = LEGACY
    if WITH_ID in version:
        fw_pointers_type = WITH_ID
    elif WITH_SHA in version:
        fw_pointers_type = WITH_SHA
    return fw_pointers_type
