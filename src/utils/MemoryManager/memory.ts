import { MemoryTypes } from "Hammer";
import * as memoryjs from "memoryjs";

export class Memory {

    private processName: string;
    private processObject: any;

    constructor(argProcessName: string) {
        this.processName = argProcessName;

        this.processObject = memoryjs.openProcess(this.processName);

        console.log(argProcessName + ': ' + this.processObject.th32ProcessID.toString());
    }

    public read(address: number, type: MemoryTypes) {
        return memoryjs.readMemory(this.processObject.handle, address, type);
    }

    public write(address: number, value: number, type: MemoryTypes) {
        memoryjs.writeMemory(this.processObject.handle, address, value, type);
    }

    public getModule(module: string) {
        return memoryjs.findModule(module, this.processObject.th32ProcessID);
    }

    public readDll(name: string) {
        return this.getModule(name).lpBaseOfDll;
    }

}

export const memory = new Memory('csgo.exe');