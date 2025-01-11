import { Body, Controller, Post } from '@nestjs/common';
import { CreateChatCompletionRequest } from './dto/create-chat-completion.resquest';
import { OpenaiService } from './openai.service';
import { ApiTags, ApiOperation, ApiResponse, ApiBody } from '@nestjs/swagger';

@ApiTags('openai')
@Controller('openai')
export class OpenaiController {
  constructor(private readonly openaiService: OpenaiService) {}

  @Post('chatCompletion')
  @ApiOperation({ summary: 'Create a chat completion' })
  @ApiResponse({
    status: 201,
    description: 'The chat completion has been successfully created.',
  })
  @ApiResponse({ status: 400, description: 'Bad Request.' })
  @ApiBody({
    schema: {
      example: {
        messages: [
          { role: 'user', content: 'Hello!' },
          { role: 'assistant', content: 'Hi! How can I help you today?' },
        ],
      },
    },
  })
  async createChatCompletion(@Body() body: CreateChatCompletionRequest) {
    return this.openaiService.createChatCompletion(body.messages);
  }
}
