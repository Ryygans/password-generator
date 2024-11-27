import random
import string,os,sys
from termcolor import colored
os.system('clear')

print(colored(""" _____
                   _.+sd$$$$$$$$$bs+._
               .+d$$$$$$$$$$$$$$$$$$$$$b+.
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$;
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$;
  $$$b       `T$b+                        :$$$$$$$BUG$$
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;
   \                            `*TP*     d$$P*******$
    \                                    :$$P'      /
     \                                  :dP'       /
      `.                               d$P       .'
[xxx]   `.                             `'      .'
          `-.                               .-'
             `-.                         .-'
                `*+-._             _.-+*'
                      `"*-------*"'
""", "red"))

print(colored('Coded By : Zann', 'green'))
print('')
print('PASSWORD GENERATOR!')
print('')
characters = string.ascii_letters + string.digits + string.punctuation

pjg = int(input(colored("Enter the length of your password: ", 'green')))
pw = ''.join(random.choices(characters, k=pjg))
print("Your password is:", pw)
