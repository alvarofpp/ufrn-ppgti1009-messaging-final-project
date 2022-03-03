import { randomUUID } from "crypto";

class OrderItem {
    id: String;
    orderId: String;
    itemId: String;
    quantity: Number;
    price: Number;
    created_at: Date;
    updated_at: Date;

    constructor() {
        if(!this.id){
            this.id = randomUUID();
        }
    }
}

export { OrderItem }