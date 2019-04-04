from leapp.actors import Actor
from leapp.libraries.actor import library
from leapp.models import StorageInfo
from leapp.tags import IPUWorkflowTag, FactsPhaseTag


class StorageScanner(Actor):
    """
    Provides data about storage settings.

    After collecting data from tools like mount, lsblk, pvs, vgs and lvdisplay, and relevant files
    under /proc/partitions and /etc/fstab, a message with relevant data will be produced.
    """

    name = 'storage_scanner'
    consumes = ()
    produces = (StorageInfo,)
    tags = (IPUWorkflowTag, FactsPhaseTag,)

    def process(self):
        self.produce(library.get_storage_info())
