import keyboard

from utils.config import config
from utils.dll import client_dll, csgo, engine_dll, getPlayer
from utils.offsets import netvars, signatures


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
    if keyboard.is_pressed(config["rank_checker_key"]):
        for i in range(1, 32):
            entity = csgo.read_int(client_dll + signatures["dwEntityList"] + i * 0x10)

            if entity:
                entity_team_id = csgo.read_int(entity + netvars["m_iTeamNum"])
                entity_i = getPlayer()
                if entity_team_id != csgo.read_int(entity_i + netvars["m_iTeamNum"]):
                    player_info = csgo.read_int(
                        (csgo.read_int(engine_dll + signatures["dwClientState"]))
                        + signatures["dwClientState_PlayerInfo"]
                    )
                    player_info_items = csgo.read_int(
                        csgo.read_int(player_info + 0x40) + 0xC
                    )
                    info = csgo.read_int(player_info_items + 0x28 + (i * 0x34))
                    name = csgo.read_string(info + 0x10)
                    if name != "GOTV":
                        playerres = csgo.read_int(
                            client_dll + signatures["dwPlayerResource"]
                        )
                        rank = csgo.read_int(
                            playerres + netvars["m_iCompetitiveRanking"] + i * 4
                        )
                        print(name + "   -->   " + ranks[rank])
