public class Array {

	public static int[] array;	
	static int size = 8;
	static int counter = 0;

	public Array() {
		set_array(size);
	}


	public static void print_Array() {
		for (int i = 0; i < size; i++) {
			if(i<counter){
				System.out.println(" ____________");
				System.out.println("|" + "__" + i + "__" + "|" + "|" + "__" + array[i] + "__" + "|");
			}
		else{
			System.out.println(" ____________");
				System.out.println("|" + "__" + i + "__" + "|" + "|" + "__" + 0 + "__" + "|");
		}
		}
	}
	
	public static void set_array(int s){
			array = new int[s];	
		}

	public static void get_value(int index) {
				if(index <counter){
					System.out.println("The value at index "+index+" " +"is"+" "+array[index]);
				}
				else{
						System.out.println("Index out of range");
					}
				}
		
				
	public static void add(int value){
					check(counter,size-1,2);
					array[counter]= value;
					counter++;
					
		}
		
	public static void check(int first,int last,int c_size){
			if(first>last){					
					int[] temp = array;
					size = size*c_size;
					set_array(size);
					for(int j=0;j<counter;j++){
							array[j]=temp[j];
						}						
				}								
		}			
								
	
	public static void insert(){
			
		}
		
		
	public static void check(){
			if(counter==size/4){
					int[] temp = array;
					set_array(size/4+1);
					size = size/2;
					for(int i=0;i<counter;i++){
							array[i]=temp[i];
						}
				}
		}
		
		
	public static void delete(){
			array[counter-1]=0;
			counter--;
		//	System.out.println(counter);
			check();			
		}
	
	public static void insert_first(int value){
			check(counter,size-1,2);
			for(int i=counter;i>0;i--){
				
				array[i]= array[i-1];
			}
			array[0]=value;
			counter++;
		}

}