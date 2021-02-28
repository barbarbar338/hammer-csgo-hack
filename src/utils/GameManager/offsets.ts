import { Offsets } from "Hammer";
import fetch from "node-fetch";

export async function getOffsets() {
    const response = await fetch('https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json');
    const data: Offsets = await response.json();

    return data;
}