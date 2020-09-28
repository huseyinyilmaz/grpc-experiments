use tonic::{transport::Server, Request, Response, Status};

use python_to_rust_simple::python_to_rust_simple_service_server::{
    PythonToRustSimpleService,
    PythonToRustSimpleServiceServer,
};

use python_to_rust_simple::{
    IncreaseRequest,
    IncreaseResponse,
};

pub mod  python_to_rust_simple {
    tonic::include_proto!("python_to_rust_simple");
}

#[derive(Debug, Default)]
pub struct IncreaseService {}

#[tonic::async_trait]
impl PythonToRustSimpleService for IncreaseService {
    async fn increase(
        &self,
        request: Request<IncreaseRequest>,
    ) -> Result<Response<IncreaseResponse>, Status> {
        let reply = IncreaseResponse {
            num: request.into_inner().num + 1,
        };

        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    let increase_service = IncreaseService::default();

    Server::builder()
        .add_service(PythonToRustSimpleServiceServer::new(increase_service))
        .serve(addr)
        .await?;

    Ok(())
}
