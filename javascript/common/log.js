export default function logger(message, loud) {
    if (loud || loud == null){
        if (typeof message == "object" || typeof message == "array"){
            console.log(JSON.stringify(message, null, 2));
        } else {
            console.log(message);
        }
    };
}