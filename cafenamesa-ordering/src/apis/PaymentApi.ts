type PaymentStatus = {
    status: String
}

class PaymentApi {
    async requestPayment (): Promise<PaymentStatus> {

        let payment = await new Promise<PaymentStatus>((resolve, reject) => {setTimeout(() => {
            resolve({status: "ok"})
        }, 2000)})
        
        return payment
    }
}

export {PaymentApi}