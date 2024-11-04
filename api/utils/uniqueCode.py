import hashlib
from core.store import store


def get_unique_code():
    try:
        import wmi
        uniqueCode = store.get("uniqueCode")
        if uniqueCode  is None:
            w = wmi.WMI()
            uniqueCode = hashlib.md5(
                w.Win32_DiskDrive()[0].SerialNumber.encode(
                    encoding='UTF-8')).hexdigest()
            store.set("uniqueCode", uniqueCode)
        return uniqueCode
    except Exception:
        return 'no unique code users'
