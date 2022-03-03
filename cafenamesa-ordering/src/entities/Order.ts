import { randomUUID } from 'crypto';

class Order {
    id: String;
    costumerId: String;
    status: String;
    price: Number;
    items ?: String[];
    created_at: Date;
    updated_at: Date;

    constructor(){
        if(!this.id){
            this.id = randomUUID();
            this.items = [];
        }
    }
}

export { Order }