import java.util.Scanner;

public class A_Phone_Desktop {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int T = scanner.nextInt(); // total test cases

    for (int i = 0; i < T; i++) {
      int x = scanner.nextInt();
      int y = scanner.nextInt();

      int screensUsed = (int) Math.ceil(y / 2.0); // minimum screens needed for 2x2
      int unusedCells = (screensUsed * 15) - (y * 4); // unused cells after placing 2x2

      if (unusedCells >= x) { // enough cells for 1x1?
        System.out.println(screensUsed);
        continue;
      }

      // otherwise add more screens
      x -= unusedCells; // use `unusedCells`, place remaining 1x1 on new screens
      screensUsed += Math.ceil((double) x / 15);
      System.out.println(screensUsed);
    }
    scanner.close();
  }
}
