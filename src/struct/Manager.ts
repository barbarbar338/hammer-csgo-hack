import { ConfigHandler, IPackage } from "Hammer";
import { getOffsets } from "../utils/GameManager/offsets"; 
import { CONFIG } from "../config";
import { readdirSync } from "fs";
import { resolve } from "path";

export class Manager {
    public config: ConfigHandler = CONFIG;
    public offsets = getOffsets();
    public packages = new Map<string, IPackage>();
    private async initPackages() {
        readdirSync(resolve("src") + "/packages").forEach((category) => {
            const packageFiles = readdirSync(
                resolve("src") + `/packages/${category}`,
            );
            packageFiles.forEach(async (name) => {
                if (name.endsWith(".map ")) return;
                const pckage: IPackage = (
                    await import (
                        resolve("src") + `/packages/${category}/${name}`
                    )
                ).default;
                console.log(pckage.name + " Loaded!")
                this.packages.set(pckage.name, pckage);
            })
        })
    }
    async init() {
        await this.initPackages()
        console.log('Hack started!')
    }
}