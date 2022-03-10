export default function formatPrice(price:number): string {
    
    let priceString = price.toFixed(2)
    
    
    let [currency, cents] = priceString.split('.');
    
    if(cents.length  < 2) {
        cents +="0"
    }

    let parsedPrice = `R$ ${currency},${cents}`

    return parsedPrice
}