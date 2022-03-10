import { GestureResponderEvent } from "react-native"

type menuListItemProps = {
    id: string,
    name: string,
    price: number,
    description: string,
    onPress?: ((event: GestureResponderEvent) => void)
}

export { menuListItemProps }