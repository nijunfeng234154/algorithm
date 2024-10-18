//前缀和差分，二维
// 1. 二维前缀和
function prefixsum(arr,x1,y1,x2,y2,c){
    s[x1][y1] += c;
    s[x2+1][y1] -= c;
    s[x1][y2+1] -= c;
    s[x2+1][y2+1] += c;
}