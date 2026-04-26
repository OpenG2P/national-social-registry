# ruff: noqa: E402
import asyncio
import logging

from .config import Settings

_config = Settings.get_config()

from openg2p_fastapi_common.app import Initializer as BaseInitializer
from openg2p_registry_core.app import Initializer as CoreInitializer

from .register_domain.models import (
    G2PRegisterIndividual, G2PRegisterHistoryIndividual,
    G2PRegisterIndividualDisability, G2PRegisterHistoryIndividualDisability,
    G2PRegisterHousehold, G2PRegisterHistoryHousehold,
    G2PRegisterProgramParticipation, G2PRegisterHistoryProgramParticipation,
    G2PRegisterPovertyScore, G2PRegisterHistoryPovertyScore,
    G2PRegisterAsset, G2PRegisterHistoryAsset,
    G2PRegisterShock, G2PRegisterHistoryShock,
    G2PRegisterConsent, G2PRegisterHistoryConsent,
    G2PRegisterGrievance, G2PRegisterHistoryGrievance,
)
from .register_domain.factory import G2PRegisterDomainFactory
from .register_domain.services import (
    G2PRegisterDomainServiceIndividual,
    G2PRegisterDomainServiceHousehold,
)

_logger = logging.getLogger(_config.logging_default_logger_name)


class Initializer(BaseInitializer):
    def initialize(self, **kwargs):
        super().initialize()
        CoreInitializer().initialize()

        G2PRegisterDomainFactory()
        G2PRegisterDomainServiceIndividual()
        G2PRegisterDomainServiceHousehold()

    def migrate_database(self, args):

        async def migrate():
            _logger.info("Migrating extensions database")

            await G2PRegisterHousehold.create_migrate()
            await G2PRegisterHistoryHousehold.create_migrate()

            await G2PRegisterIndividual.create_migrate()
            await G2PRegisterHistoryIndividual.create_migrate()

            await G2PRegisterIndividualDisability.create_migrate()
            await G2PRegisterHistoryIndividualDisability.create_migrate()

            await G2PRegisterProgramParticipation.create_migrate()
            await G2PRegisterHistoryProgramParticipation.create_migrate()

            await G2PRegisterPovertyScore.create_migrate()
            await G2PRegisterHistoryPovertyScore.create_migrate()

            await G2PRegisterAsset.create_migrate()
            await G2PRegisterHistoryAsset.create_migrate()

            await G2PRegisterShock.create_migrate()
            await G2PRegisterHistoryShock.create_migrate()

            await G2PRegisterConsent.create_migrate()
            await G2PRegisterHistoryConsent.create_migrate()

            await G2PRegisterGrievance.create_migrate()
            await G2PRegisterHistoryGrievance.create_migrate()

        asyncio.run(migrate())
