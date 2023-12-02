# Insights day 1

Insights
1. Consider manipulating input data
instead of accepting it as is
2. "get last and first digit" can be
interpreted less rigidly, get all digits
and pick out last first and last. 
Formally: if f(org_inp) = (first, last)
z(alt_input) = (first, last) and h(org_inp) = alt_inp then
z(h(org_inp)) = (first, last) so if z and h are 
minimally complex then z and h are preferred over f.
and in most cases f can be broken down in similar ways
just have to not tunnel vision on finding f
3. can use dict.get to get the function that maps from
the created dicts key/vals
4. (?=...) to match ahead without consuming, important
in this case since (1|one|two|three|eight) for e.g.
1twothreeight would consume [1twothree]ight not
matching the actual last dig eight