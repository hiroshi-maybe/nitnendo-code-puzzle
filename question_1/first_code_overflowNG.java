public class Nintendo01NG {
       
  public static void main(String[] args) {
    long i=0;
    while(true) {
      if (Math.pow(i,17)%3569==915) {
	System.out.println(i);
	break;
      }
      i+=1;
    }
  }
}