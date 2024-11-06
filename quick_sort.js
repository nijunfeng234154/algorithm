
// javascript代码实现快速排序
function quick_sort(arr, left = 0, right = arr.length - 1) {
    if (left >= right) return;

    let i = left, j = right;
    const key = arr[left];

    while (i < j) {
        while (arr[j] > key) j--;
        while (arr[i] < key) i++;
        if(i<j){
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    quick_sort(arr, left, j);
    quick_sort(arr, j + 1, right);
}

function merge_sort(arr, l, r){
    if (l >= r) return;

    let mid = l + r >>1;
    
    merge_sort(arr,l,mid);
    merge_sort(arr,mid+1,r);

    let k=0;
    var i,j;
    while(i<=mid && j<=r){
        if(arr[i] < arr[j]){
            temp[k++] = arr[i++];
        }
        else{
            temp[k++] = arr[j++];
        }
}  
    while(i<=mid) temp[k++] = arr[i++];
    while(j<=r) temp[k++] = arr[j++];

    for(i=l,j=0;i<=r;i++,j++){
        arr[i] = temp[j];
    }
}

// test
var arr = [1, 3, 2, 5, 4, 6, 7, 9, 8];
quick_sort(arr,0,arr.length-1);
console.log(arr);