import { OrderItem } from "entities/OrderItem";

interface CreateOrderItemDTO {
    orderId: String;
    itemId: String;
    quantity: Number;
    price: Number;
}

class OrderItemsRepository {
    private orderItems: OrderItem[];

    constructor() {
        this.orderItems = []
    }

    create({orderId, itemId, quantity, price}: CreateOrderItemDTO): OrderItem {
        const orderItem = new OrderItem();

        Object.assign(orderItem, {
            orderId,
            itemId,
            price,
            created_at: new Date(),
            updated_at: new Date()
        })

        this.orderItems.push(orderItem);

        return orderItem;
    }

    getItemsByOrderId(orderId: String): OrderItem[]{
        const orderItems = this.orderItems.filter(orderItem => orderId === orderItem.orderId);
        return orderItems;
    }
}

export { OrderItemsRepository };