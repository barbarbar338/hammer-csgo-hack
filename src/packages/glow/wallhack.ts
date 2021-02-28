import { PackageArgs, IPackage, Offsets } from "Hammer";
import { memory } from "../../utils/MemoryManager/memory";

  
export interface Color {
    r: number;
    g: number;
    b: number;
    a: number;
}

export function glow(entity: number, glowPointer: number, color: Color, offsets: Offsets) {
    const glowIndex = memory.read(entity + offsets.netvars.m_iGlowIndex, 'dword');

    memory.write(glowPointer + (glowIndex * 0x38 + 0x4), color.r, "float");
    memory.write(glowPointer + (glowIndex * 0x38 + 0x8), color.g, "float");
    memory.write(glowPointer + (glowIndex * 0x38 + 0xC), color.b, "float");
    memory.write(glowPointer + (glowIndex * 0x38 + 0x10), color.a, "float");
    memory.write(glowPointer + (glowIndex * 0x38 + 0x24), 1, "bool");
    memory.write(glowPointer + (glowIndex * 0x38 + 0x25), 0, "bool");
    memory.write(glowPointer + (glowIndex * 0x38 + 0x26), 0, "bool");
}

const AimBotPackage: IPackage = {
    name: "WallHack",
    category: "glow",
    async execute({
        player,
        entity,
        offsets,
    }: PackageArgs): Promise<void> {
        const clientModule = memory.getModule('client_panorama.dll');
        const engineModule = memory.getModule('engine.dll');
        while (true) {
            const localPlayer = memory.read(clientModule.modBaseAddr + offsets.signatures.dwLocalPlayer, 'dword');
            const glowPointer = memory.read(clientModule.modBaseAddr + offsets.signatures.dwGlowObjectManager, 'dword');
            if (!localPlayer) return;
            for (let i = 0; i < 32; i++) {
                const currentEntity = memory.read(clientModule.modBaseAddr + offsets.signatures.dwEntityList + (i - 1) * 0x10, 'dword');
                const isDormant = memory.read(currentEntity + offsets.signatures.m_bDormant, 'boolean');

                if (isDormant) return;

                let color: Color = {r: 1, b: 0, g: 0, a: 1};
                
                glow(currentEntity, glowPointer, color, offsets);
            }
        }
    }
}


export default AimBotPackage;