
enum HockeyPlayer {
	Center,
	Wing,
	Defence,
	Goalie
}

fn next_player(position: HockeyPlayer){
   
} 

fn main(){
    let position= HockeyPlayer::Defence;
    next_player(position)
}



//1
enum Clock{
	Sundail(u8),
	Digital(u8,u8),
	Analog(u8,u8,u8),
}

fn tell_time(clock: Clock){
	match clock{
		Clock::Sundail(hours) => 
		    println!(" it is about {} o'clock",hours)
		Clock::Digital(hours,minutes) => 
		    println!("it is {} minutes past {}",minutes,hours),
		Clock::Analog(hours,minutes,seconds) => 
		    println!("it is {} minutes and {} seconds past {}",minutes,seconds,hours)		        
	}
}

fn main(){
	tell_time(Clock::Analog(9,25,45))
}

//2
enum Clock{
	Sundail(hours:u8),
	Digital(hours:u8,minutes:u8),
	 Analog(hours:u8,minutes:u8,seconds:u8),
}

fn tell_time(clock: Clock){
	match clock{
		Clock::Sundail(hours) => 
		    println!(" it is about {} o'clock",hours)
		Clock::Digital(hours,minutes) => 
		    println!("it is {} minutes past {}",minutes,hours),
		Clock::Analog(hours,minutes,seconds) => 
		    println!("it is {} minutes and {} seconds past {}",minutes,seconds,hours)		        
	}
}

fn main(){
	let clock = Clock::Analog{
		hours: 9,
		minutes:25,
		seconds: 46
	}
}



struct HockeyPlayer {
    name: String,
    number: u8,
    position: HockeyPlayer,
    goals_ytd: u8
}


fn main(){
   let player= HockeyPlayer{
   	  name: String::from("Bryan Rust"),
   	  number:17,
   	  position: HockeyPlayer::Wing,
   	  goals_ytd: 7,
   }
   println!("{} has scored {} goals this season",player.name,player.goals_ytd);
}


fn main(){
   let mut player= HockeyPlayer{
   	  name: String::from("Bryan Rust"),
   	  number:17,
   	  position: HockeyPlayer::Wing,
   	  goals_ytd: 7,
   }
   println!("{} has scored {} goals this season",player.name,player.goals_ytd);
}

struct Trigangle(u32,u32,u32);
fn is_equilateral(triangle: Triangle)-> bool{
    triangle.0 == triangle.1 && triangle.1==triangle.2
}

fn main(){
    let triangle = Triangle(3,4,5);
    is_equilateral(triangle)
}




struct Traingle(u8,u8,u8)
fn main(){
	println!("hello world")
}
ownsership

fn say(s:String){
	println!("I say, {}",s);
}
fn main(){
	let a= String::from("hello");
	say(a)

	// #ownsership is transferred to say function argument a.

}


fn heart()-> String{
	String::from("heee giving ownsership")
}


cloning

a.clone()  // creates copy of a.



fn succeed(p: &String){
    println!("check {} ",p)
}

enum Twoplayer{
    Playerone(u8),
    Playertwo(u8)
}

fn main() {
    println!("Hello, world!");
    let p=String::from("vishal");
    succeed(&p);
    
    let player1=Twoplayer::Playerone(51);
    let player2=Twoplayer::Playertwo(50);
    
    match player1{
        Twoplayer::Playerone(score)=>{
            println!("hello player one {}",score);
        },
        Twoplayer::Playertwo(score)=>{
            println!("hello player two{}",score);
        }        
    }
    
        match player2{
        Twoplayer::Playerone(score)=>{
            println!("hello player one {}",score);
        },
        Twoplayer::Playertwo(score)=>{
            println!("hello player two{}",score);
        }        
    }
    
    
}