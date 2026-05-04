from memory.archive import MemoryArchive

def test_memory_storage():
    archive = MemoryArchive()
    archive.store({"experience": "test"})
    assert len(archive.retrieve_all()) == 1
