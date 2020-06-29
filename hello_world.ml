open! Core

let fact x =
  let rec loop acc y =
    let multiplied =
      Z.( * ) acc y
    in
    if Z.equal y x
    then multiplied
    else loop multiplied (Z.( + ) y Z.one)
  in
  loop Z.one Z.one

let _ = fact

let rec ack m n ~print_func =
  if Z.equal m Z.zero
  then (
    let result = Z.succ n in
    print_func (Z.to_string result);
    result)
  else if Z.equal n Z.zero
  then (
    let m_pred = Z.pred m in 
    print_func ("A(" ^ Z.to_string m_pred ^ ",1)");
    ack m_pred Z.one ~print_func
  )
  else
    let m_pred = Z.pred m in
    print_func ("A(" ^ Z.to_string m_pred ^ ",A(" ^ Z.to_string m ^ ","
              ^ Z.to_string (Z.pred n) ^ "))");
    let sub_result =
      ack m (Z.pred n) ~print_func:(fun s ->
          print_func ("A(" ^ Z.to_string m_pred ^ "," ^ s ^ ")"))
    in
    ack m_pred sub_result ~print_func

let () =
  let m = Z.of_string (Sys.get_argv ()).(1) in
  let n = Z.of_string (Sys.get_argv ()).(2) in
  print_endline ("A(" ^ Z.to_string m ^ "," ^ Z.to_string n ^ ")");
  print_endline
    (
      Z.to_string
        (
          ack m n
            ~print_func:(fun s -> print_endline ("=" ^ s))))
    
