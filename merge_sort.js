function merge_sort(arr,l,r){
    if (l>=r) return;

    let mid = Math.floor((l + r) / 2);
    merge_sort(arr,l,mid);
    merge_sort(arr,mid+1,r);

    let i=l,j=mid+1;
    let temp = [];
    let k=0;
    while(i<=mid&&j<=r){
        if(arr[i]<=arr[j]){
            temp[k++] = arr[i++];
        }else{
            temp[k++] = arr[j++];
        }
    }
    while(i<=mid) temp[k++] = arr[i++];
    while(j<=r) temp[k++] = arr[j++];

    for(i=l,k=0;i<=r;i++,k++){
        arr[i] = temp[k];
}
}
function quick_sort(arr,l,r){
    if(l>=r) return;

    let mid = arr[l];
    let i=l,j=r;
    while(i<j){
        while(arr[i]<mid) i++;
        while(arr[j]>mid) j--;
        if(i<j){
            [arr[i],arr[j]] = [arr[j],arr[i]];
        }
    }
    quick_sort(arr,l,j);
    quick_sort(arr,j+1,r);
}


var arr = [1, 3, 2, 5, 4, 6, 7, 9, 8];
quick_sort(arr,0,arr.length-1);
console.log(arr);