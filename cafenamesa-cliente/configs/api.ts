import database from "./fakeDatabase/itens.database.json";

const itemsAPI = {
    getItemById: function(id: string){
        return database.find((item) => item.id == id)
    },
    getAllItemsByMenu: function(){
        const allItemsByGroup: { title: string; data: { id: string; name: string; price: number; description: string; }[]; }[] = []

        for (let item of database) {
            const menuGroup = item.menu;
            const existentGroup = allItemsByGroup.find((group) => group.title == menuGroup);

            if(existentGroup){
                existentGroup.data.push({id: item.id, name: item.name, price: item.price, description: item.description})
            } else {
                allItemsByGroup.push({
                    title: menuGroup,
                    data: [
                        {id: item.id, 
                        name: item.name,
                        price: item.price,
                        description: item.description}
                    ]
                })
            }
        }

        return allItemsByGroup;
    }
}

export { itemsAPI }