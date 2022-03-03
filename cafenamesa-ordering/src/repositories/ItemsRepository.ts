import { Item } from "entities/Item";

interface CreateItemDTO {
    name: String,
    description: String,
    price: Number;
    menu_id: String;
}

class ItemsRepository {
    repository: Item[];

    constructor() {
        this.repository = []
    }

    create({name, description, menu_id, price}: CreateItemDTO) {
        const item = new Item();

        Object.assign(item, {
            name,
            menu_id,
            price,
            description,
            created_at: new Date(),
            updated_at: new Date()
        })
    }

    getPriceById(id: String){
        return 
    }
}