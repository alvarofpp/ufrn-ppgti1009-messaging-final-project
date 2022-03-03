import { Channel, connect, Connection, Replies } from "amqplib";
//queue.js
function connectQueue(){
    return connect("amqp://ppgti:ppgti@localhost:5672/ppgti_host")
                             .then(conn => conn.createChannel());
  }
   
function createExchange(channel: Channel, exchange: string): Promise<Channel>{
    return new Promise<Channel>((resolve, reject) => {
        try{
        channel.assertExchange(exchange, 'direct', { durable: true });
        resolve(channel);
        }
        catch(err){ reject(err) }
    });
}
   
  function sendToExchange(exchange: string, message: Object){
    connectQueue()
      .then(channel => createExchange(channel, exchange))
      .then(channel => channel.publish(exchange,'green' ,Buffer.from(JSON.stringify(message))))
      .catch(err => console.log(err))
  }
   
//   function consume(queue, callback){
//     connect()
//       .then(channel => createQueue(channel, queue))
//       .then(channel => channel.consume(queue, callback, { noAck: true }))
//       .catch(err => console.log(err));
//   }



// async function sendMessageToQueue(conn: Connection | Promise<Connection>, msg: String) {
//     let channel: Channel;
//     const connection = await conn;

//     try {    
//         channel = await connection.createChannel();   
//     } catch (error) {
//         console.error("Create channel error:" + error);
//     }
    
//     if(channel){
//         await channel.assertExchange('test-exchange', 'direct');
//         channel.publish('test-exchange', 'green', Buffer.from(msg));
//     }

    // setTimeout(function() {
    //     connection.close();
    //     process.exit(0);
    //   }, 500);
// }

export { sendToExchange }