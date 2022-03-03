import { randomUUID } from "crypto";

class Menu {
    id: String;
    name: String;
    items: String[];
    created_at: Date;
    updated_at: Date;

    constructor(){
        if(!this.id){
            this.id = randomUUID();
        }
    }
}

export { Menu }