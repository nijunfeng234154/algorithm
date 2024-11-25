/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    var r=0,l=0
    if(s=="") return true
    if(t=="") return false
    while(l<t.length){
        if(r==s.length-1&&s[r]==t[l]) return true
        if(s[r]==t[l]) r++
        l++
    }
    return false
};