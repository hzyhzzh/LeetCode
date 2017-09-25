class Solution {
    public boolean isIsomorphic(String s, String t) {
       HashMap<String , String> map = new HashMap<String , String>();
       String result = "";
       for(int i = 0;i<s.length();++i) {
           if(map.containsKey(s[i])){
               result += map.get(s[i]);
           } 
           else {
               map.put(s[i],t[i]);
           }
       }
        
    }
}