import { PaymentApi } from "apis/PaymentApi";
import { OrderItemsRepository } from "repositories/OrdersItemsRepository";
import { OrdersRepository } from "repositories/OrdersRepository";

import express from "express";
import { sendToExchange } from "configs/amqpConnection";

const ordersRepository = new OrdersRepository();
const orderItemsRepository = new OrderItemsRepository();

const paymentApi = new PaymentApi();

const app = express();
app.use(express.json());

app.post('/orders', async (request, response) => {
    const { costumerId, price, orderItems } = request.body;

    const {status: paymentStatus} = await paymentApi.requestPayment();

    if(paymentStatus === "ok"){
        const order = ordersRepository.create({costumerId, price});

        for (let item of orderItems) {
            const { itemId, quantity, price } = item;

            const orderItem = orderItemsRepository.create({
                orderId: order.id,
                itemId,
                quantity,
                price
            })

            order.items.push(orderItem.id);
        }
        
        sendToExchange("order-status-exchange", {status: "Order placed"});
        return response.status(200).json({order});
    }

    return response.status(400).send("Payment not aproved");
})

app.listen(3000, () => {
    console.log("Server started!")
})