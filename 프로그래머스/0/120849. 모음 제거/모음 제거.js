function solution(my_string) {
    let delArr = ['a', 'e', 'i', 'o', 'u']
    let arr = my_string.split("").filter(arr => !delArr.includes(arr));
    
    return arr.join('');
    
}