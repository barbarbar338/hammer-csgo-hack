import keyboard
from utils.dll import csgo, client_dll, engine_dll
from utils.offsets import (
    dwEntityList,
    m_iTeamNum,
    dwLocalPlayer,
    dwClientState,
    dwClientState_PlayerInfo,
    dwPlayerResource,
    m_iCompetitiveRanking,
)
from utils.config import rank_checker_key


def rank():
    ranks = [
        "Unranked",
        "Silver I",
        "Silver II",
        "Silver III",
        "Silver IV",
        "Silver Elite",
        "Silver Elite Master",
        "Gold Nova I",
        "Gold Nova II",
        "Gold Nova III",
        "Gold Nova Master",
        "Master Guardian I",
        "Master Guardian II",
        "Master Guardian Elite",
        "Distinguished Master Guardian",
        "Legendary Eagle",
        "Legendary Eagle Master",
        "Supreme Master First Class",
        "The Global Elite",
    ]
    if keyboard.is_pressed(rank_checker_key):
        for i in range(1, 32):
            entity = csgo.read_int(client_dll + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = csgo.read_int(entity + m_iTeamNum)
                entity_i = csgo.read_int(client_dll + dwLocalPlayer)
                if entity_team_id != csgo.read_int(entity_i + m_iTeamNum):
                    player_info = csgo.read_int(
                        (csgo.read_int(engine_dll + dwClientState))
                        + dwClientState_PlayerInfo
                    )
                    player_info_items = csgo.read_int(
                        csgo.read_int(player_info + 0x40) + 0xC
                    )
                    info = csgo.read_int(player_info_items + 0x28 + (i * 0x34))
                    name = csgo.read_string(info + 0x10)
                    if name != "GOTV":
                        playerres = csgo.read_int(client_dll + dwPlayerResource)
                        rank = csgo.read_int(playerres + m_iCompetitiveRanking + i * 4)
                        print(name + "   -->   " + ranks[rank])
