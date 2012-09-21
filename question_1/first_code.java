import java.math.BigDecimal;

public class Nintendo01 {
  static final BigDecimal divider = new BigDecimal(3569);
  static final BigDecimal adder = new BigDecimal(1);
  public static void main(String[] args) {
    BigDecimal i = new BigDecimal(0);
    while(true) {
      BigDecimal j=i.pow(17);
      j=j.remainder(divider);
      if (j.intValue()==915) {
	System.out.println(i);
	break;
      }
      i=i.add(adder);
      System.out.println(i);
    }
  }
}