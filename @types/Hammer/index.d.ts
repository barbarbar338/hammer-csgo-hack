declare module "Hammer" {
    export interface Offsets {
        signatures: {
            anim_overlays: number;
            clientstate_choked_commands: number;
            clientstate_delta_ticks: number;
            clientstate_last_outgoing_command: number;
            clientstate_net_channel: number;
            convar_name_hash_table: number;
            dwClientState: number;
            dwClientState_GetLocalPlayer: number;
            dwClientState_IsHLTV: number;
            dwClientState_Map: number;
            dwClientState_MapDirectory: number;
            dwClientState_MaxPlayer: number;
            dwClientState_PlayerInfo: number;
            dwClientState_State: number;
            dwClientState_ViewAngles: number;
            dwEntityList: number;
            dwForceAttack: number;
            dwForceAttack2: number;
            dwForceBackward: number;
            dwForceForward: number;
            dwForceJump: number;
            dwForceLeft: number;
            dwForceRight: number;
            dwGameDir: number;
            dwGameRulesProxy: number;
            dwGetAllClasses: number;
            dwGlobalVars: number;
            dwGlowObjectManager: number;
            dwInput: number;
            dwInterfaceLinkList: number;
            dwLocalPlayer: number;
            dwMouseEnable: number;
            dwMouseEnablePtr: number;
            dwPlayerResource: number;
            dwRadarBase: number;
            dwSensitivity: number;
            dwSensitivityPtr: number;
            dwSetClanTag: number;
            dwViewMatrix: number;
            dwWeaponTable: number;
            dwWeaponTableIndex: number;
            dwYawPtr: number;
            dwZoomSensitivityRatioPtr: number;
            dwbSendPackets: number;
            dwppDirect3DDevice9: number;
            find_hud_element: number;
            force_update_spectator_glow: number;
            interface_engine_cvar: number;
            is_c4_owner: number;
            m_bDormant: number;
            m_flSpawnTime: number;
            m_pStudioHdr: number;
            m_pitchClassPtr: number;
            m_yawClassPtr: number;
            model_ambient_min: number;
            set_abs_angles: number;
            set_abs_origin: number;
        }
        netvars: {
            cs_gamerules_data: number;
            m_ArmorValue: number;
            m_Collision: number;
            m_CollisionGroup: number;
            m_Local: number;
            m_MoveType: number;
            m_OriginalOwnerXuidHigh: number;
            m_OriginalOwnerXuidLow: number;
            m_SurvivalGameRuleDecisionTypes: number;
            m_SurvivalRules: number;
            m_aimPunchAngle: number;
            m_aimPunchAngleVel: number;
            m_angEyeAnglesX: number;
            m_angEyeAnglesY: number;
            m_bBombPlanted: number;
            m_bFreezePeriod: number;
            m_bGunGameImmunity: number;
            m_bHasDefuser: number;
            m_bHasHelmet: number;
            m_bInReload: number;
            m_bIsDefusing: number;
            m_bIsQueuedMatchmaking: number;
            m_bIsScoped: number;
            m_bIsValveDS: number;
            m_bSpotted: number;
            m_bSpottedByMask: number;
            m_bStartedArming: number;
            m_bUseCustomAutoExposureMax: number;
            m_bUseCustomAutoExposureMin: number;
            m_bUseCustomBloomScale: number;
            m_clrRender: number;
            m_dwBoneMatrix: number;
            m_fAccuracyPenalty: number;
            m_fFlags: number;
            m_flC4Blow: number;
            m_flCustomAutoExposureMax: number;
            m_flCustomAutoExposureMin: number;
            m_flCustomBloomScale: number;
            m_flDefuseCountDown: number;
            m_flDefuseLength: number;
            m_flFallbackWear: number;
            m_flFlashDuration: number;
            m_flFlashMaxAlpha: number;
            m_flLastBoneSetupTime: number;
            m_flLowerBodyYawTarget: number;
            m_flNextAttack: number;
            m_flNextPrimaryAttack: number;
            m_flSimulationTime: number;
            m_flTimerLength: number;
            m_hActiveWeapon: number;
            m_hMyWeapons: number;
            m_hObserverTarget: number;
            m_hOwner: number;
            m_hOwnerEntity: number;
            m_iAccountID: number;
            m_iClip1: number;
            m_iCompetitiveRanking: number;
            m_iCompetitiveWins: number;
            m_iCrosshairId: number;
            m_iDefaultFOV: number;
            m_iEntityQuality: number;
            m_iFOVStart: number;
            m_iGlowIndex: number;
            m_iHealth: number;
            m_iItemDefinitionIndex: number;
            m_iItemIDHigh: number;
            m_iMostRecentModelBoneCounter: number;
            m_iObserverMode: number;
            m_iShotsFired: number;
            m_iState: number;
            m_iTeamNum: number;
            m_lifeState: number;
            m_nFallbackPaintKit: number;
            m_nFallbackSeed: number;
            m_nFallbackStatTrak: number;
            m_nForceBone: number;
            m_nTickBase: number;
            m_rgflCoordinateFrame: number;
            m_szCustomName: number;
            m_szLastPlaceName: number;
            m_thirdPersonViewAngles: number;
            m_vecOrigin: number;
            m_vecVelocity: number;
            m_vecViewOffset: number;
            m_viewPunchAngle: number;
        }
    }

    export type MemoryTypes = (
        "byte" |
        "int" |
        "int32" |
        "uint32" |
        "int64" |
        "uint64" |
        "dword" |
        "short" |
        "long" |
        "float" |
        "double" |
        "bool" |
        "boolean" |
        "ptr" |
        "pointer" |
        "str" |
        "string" |
        "vec3" |
        "vector3" |
        "vec4" |
        "vector4"
    )

    export interface PackageArgs {
        player: any;
        entity: any;
		offsets: Offsets;
	}

    export interface IPackage {
		name: string;
		category: string;
		execute: (packageArgs: PackageArgs) => Promise<void>;
	}

    export type AimTypes = (
        "Lock" |
        "Silent" |
        "SilentRCS" |
        "Legit"
    ) 

    export type GlowOpacityTypes = (
        "Low" |
        "Medium" |
        "High" |
        "Ultra"
    )

    export interface ConfigHandler {
        license: string;
        inGame: {
            aim: {
                fov: number;
                force_shoot: boolean;
                type: AimTypes;
                key: import('keycode').codes;
            }
            glow: {
                ct_glow: {
                    red: number;
                    green: number;
                    blue: number;
                    opacity: GlowOpacityTypes;
                }
                t_glow: {
                    red: number;
                    green: number;
                    blue: number;
                    opacity: GlowOpacityTypes;
                }
            }
            fov: {
                fov_rate: number;
            }
            triggerbot: {
                delay: number | undefined
            }
            misc: {
                cancel_flash: boolean;
                radar: boolean;
                rank_checker: boolean;
            }
        }   
    }
}