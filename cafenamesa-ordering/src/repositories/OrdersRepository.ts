import { Order } from "entities/Order";

interface CreateOrderDTO {
    costumerId: String,
    price: Number
}

class OrdersRepository {
    private orders: Order[];

    constructor() {
        this.orders = []
    }

    create({costumerId, price}: CreateOrderDTO): Order {
        const order = new Order();

        const status = "Waiting to accept"
        Object.assign(order, {
            costumerId,
            status,
            price,
            created_at: new Date(),
            updated_at: new Date()
        })

        this.orders.push(order);

        return order;
    }

    getOrdersByCostumerId(costumerId: String): Order[]{
        const orders = this.orders.filter(order => costumerId === order.costumerId);
        return orders;
    }
}

export { OrdersRepository };