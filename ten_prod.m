function out = ten_prod(a,b)
  nj = size(a)(1);
  nk = size(a)(2);
  nl = size(b)(1);
  nm = size(b)(2);
  for j=1:nj
    for k=1:nk
      for l=1:nl
        for m=1:nm
          out((j-1)*size(b)(1)+l,(k-1)*size(a)(2) +m) = a(j, k)*b(l, m);
        end
      end
    end
  end
end