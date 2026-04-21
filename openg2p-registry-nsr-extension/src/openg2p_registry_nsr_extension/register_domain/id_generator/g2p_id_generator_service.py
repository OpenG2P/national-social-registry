from openg2p_fastapi_common.service import BaseService
from openg2p_registry_core.interfaces import G2PIdGeneratorInterface, IdAffix
from openg2p_registry_core.models.g2p_register import G2PRegister


class G2PIdGeneratorService(BaseService, G2PIdGeneratorInterface):

    def generate_prefix_suffix(
        self, g2p_register: G2PRegister, register_mnemonic: str
    ) -> IdAffix:
        mnemonic = (register_mnemonic or "").lower()

        if mnemonic == "individual":
            return IdAffix(prefix="IND-", suffix="")
        if mnemonic == "household":
            return IdAffix(prefix="HH-", suffix="")
        if mnemonic == "programparticipation":
            return IdAffix(prefix="PP-", suffix="")
        if mnemonic == "povertyscore":
            return IdAffix(prefix="PMT-", suffix="")
        if mnemonic == "asset":
            return IdAffix(prefix="AST-", suffix="")
        if mnemonic == "shock":
            return IdAffix(prefix="SHK-", suffix="")
        if mnemonic == "consent":
            return IdAffix(prefix="CNS-", suffix="")
        if mnemonic == "grievance":
            return IdAffix(prefix="GRV-", suffix="")
        if mnemonic == "verificationhistory":
            return IdAffix(prefix="VER-", suffix="")

        return IdAffix(prefix="DEFAULT-", suffix="")
