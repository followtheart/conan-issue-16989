//#include <ATen/ATen.h>
// #include <torch/torch.h>
#include <iostream>
//#include <c10/util/Exception.h>
void test_aten(){
//at::Tensor a = at::ones({2, 2}, at::kInt);
//at::Tensor b = at::randn({2, 2});
//auto c = a + b.to(at::kInt);
//std::cout << "result c:" << c << std::endl;
}

void test_torch() {
	try
	{
		//torch::Tensor foo = torch::rand({ 12, 12 });

		//// assert foo is 2-dimensional and holds floats.
		//auto foo_a = foo.accessor<float, 2>();
		//float trace = 0;

		//for (int i = 0; i < foo_a.size(0); i++) {
		//	// use the accessor foo_a to get tensor data.
		//	trace += foo_a[i][i];
		//}
		std::cout << "test" << std::endl;
	}
	catch (const std::exception& e)
	{
		std::cout << e.what() << std::endl;
	}

}