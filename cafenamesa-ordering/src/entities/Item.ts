import { randomUUID } from "crypto";

class Item {
    id: String;
    name: String;
    description: String;
    price: Number;
    available: Boolean;
    menu_id: String;
    created_at: String;
    updated_at: String;

    constructor() {
        if(!this.id){
            this.id = randomUUID();
            this.available = true;
        }
    }
}

export { Item };