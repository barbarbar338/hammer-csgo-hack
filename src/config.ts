import { ConfigHandler } from "Hammer";

export const CONFIG: ConfigHandler = {
    license: "",
    inGame: {
        aim: {
            fov: 1.0,
            force_shoot: true,
            type: "Lock",
            key: "ctrl",
        },
        glow: {
            ct_glow: {
                blue: 2.0,
                green: 0.0,
                red: 2.0,
                opacity: "High",
            },
            t_glow: {
                blue: 0.0,
                green: 2.0,
                red: 2.0,
                opacity: "High",
            }
        },
        fov: {
            fov_rate: 120,
        },
        misc: {
            cancel_flash: true,
            radar: true,
            rank_checker: true,
        },
        triggerbot: {
            delay: 1,
        }
    }
}